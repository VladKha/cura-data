import time

from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel, Field
from openai import OpenAI


class DataErrorAnalysis(BaseModel):
    class DataError(BaseModel):
        error_phrase: str = Field(description="exact sentence or phrase from the original text")
        error_short_summary: str = Field(description="couple of words or short phrase that describes the inaccuracy")
        why_wrong: str = Field(description="short and clear, bullet point explanation why it's wrong with references")
        suggested_fix: str = Field(description="proposed fix to the inaccurate information")
        references: list[str] = Field(
            description="The list of reference URLs or citations mentioned in the why_wrong or suggested_fix, if present"
        )

    errors: list[DataError]


ANALYSIS_PROMPT = """
You are an expert in detecting errors and inconsistencies in data.
You will be provided with a Wikipedia URL.
Your goal will be to find at least one error on the page and provide response with corresponding analysis.
"""

def find_wikipedia_errors_advanced(
    url: str,
    model: str = "gpt-5",
    reasoning_effort: str = "high",
) -> DataErrorAnalysis:
    client = OpenAI()
    response = client.responses.parse(
        model=model,  # gpt-5 | gpt-5-nano
        reasoning={"effort": reasoning_effort},  # high | low
        tools=[{"type": "web_search"}],
        input=[
            {"role": "system", "content": ANALYSIS_PROMPT},
            {"role": "user", "content": f"Wikipedia URL: {url}"},
        ],
        text_format=DataErrorAnalysis,
    )
    return response.output_parsed


def main():
    url = "https://simple.wikipedia.org/wiki/Tartar_sauce"
    start = time.perf_counter()
    analysis = find_wikipedia_errors_advanced(url)
    total_time = time.perf_counter() - start
    for data_error in analysis.errors:
        print("error_phrase:", data_error.error_phrase)
        print("error_short_summary:", data_error.error_short_summary)
        print("why_wrong:", data_error.why_wrong)
        print("suggested_fix:", data_error.suggested_fix)
        print("references:", data_error.references)
        print("-" * 80)
    print(f"Request duration: {total_time:.2f} seconds")


if __name__ == "__main__":
    main()
# error_phrase: Tartar sauce (tartare in the United Kingdom and Australia)
# error_short_summary: UK/Australia call it “tartare sauce,” not just “tartare”
# why_wrong: In British and Australian usage the condiment is called “tartare sauce” (including the word “sauce”); “tartare” alone is ambiguous (it can refer to raw preparations like steak tartare). Major dictionaries list “tartare sauce” as the British variant, and Australian food labeling also uses “Tartare Sauce.” citeturn4search0turn4search1turn9search4
# suggested_fix: Change to: “Tartar sauce (called ‘tartare sauce’ in the United Kingdom and Australia) is a mayonnaise‑based sauce.”
# references: ['https://dictionary.cambridge.org/dictionary/english/tartar-sauce', 'https://www.britannica.com/dictionary/tartar-sauce', 'https://www.masterfoods.com.au/products/masterfoods-traditional-tartare-sauce-220g']
# --------------------------------------------------------------------------------
# error_phrase: The word Tartar is a Turkic word.
# error_short_summary: Misstated etymology; ‘Tartar’ isn’t a Turkic word
# why_wrong: The English word “Tartar” is a Western/Latinized form influenced by Tartarus and derived via Medieval Latin/Old French from the ethnonym “Tatar.” The sauce’s name comes from French “sauce tartare.” “Tatar” (the people) is Turkic, but “Tartar” itself is not a Turkic word. citeturn8search0turn7search2turn10search0
# suggested_fix: Replace with: “The sauce’s name comes from French ‘sauce tartare’; the term ‘tartare’ refers to the Tatars, a Turkic people. ‘Tartar’ is the older Western form influenced by the Latin word Tartarus.”
# references: ['https://www.etymonline.com/word/tartar', 'https://www.merriam-webster.com/word-of-the-day/tartar-2012-11-20', 'https://www.britannica.com/topic/steak-tartare']
# --------------------------------------------------------------------------------
# Request duration: 235.20 seconds