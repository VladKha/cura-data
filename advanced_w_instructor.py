import time

from charset_normalizer.md import lru_cache
from dotenv import load_dotenv
load_dotenv()

import instructor
from pydantic import BaseModel, Field


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

def find_wikipedia_errors_advanced_2(
    url: str,
    provider: str = "openai/gpt-5", # gpt-5 | gpt-5-nano
    mode: instructor.Mode = instructor.Mode.RESPONSES_TOOLS_WITH_INBUILT_TOOLS,
    reasoning_effort: str = "high", # high | low
) -> DataErrorAnalysis:
    client = instructor.from_provider(provider, mode=mode)
    request_kwargs = dict(
        reasoning={"effort": reasoning_effort},  # high | low
        tools=[{"type": "web_search"}],
        input=[
            {"role": "system", "content": ANALYSIS_PROMPT},
            {"role": "user", "content": f"Wikipedia URL: {url}"},
        ],
        response_model=DataErrorAnalysis,
    )
    analysis = client.responses.create(**request_kwargs)
    return analysis
    # return {
    #   "errors": [
    #     {
    #       "error_phrase": "Tartar sauce (tartare in the United Kingdom and Australia)",
    #       "error_short_summary": "British/Australian name missing “sauce”",
    #       "why_wrong": "- Standard British/Commonwealth usage is “tartare sauce,” not just “tartare.”\n- Major dictionaries list the British variant explicitly as “tartare sauce.”\n- En‑Wikipedia also notes the UK/Commonwealth spelling as “tartare sauce.”",
    #       "suggested_fix": "Change to: “Tartar sauce (called ‘tartare sauce’ in the United Kingdom and Australia).”",
    #       "references": [
    #         "https://dictionary.cambridge.org/dictionary/english/tartar-sauce",
    #         "https://www.merriam-webster.com/dictionary/tartar%20sauce",
    #         "https://www.britannica.com/dictionary/tartar-sauce",
    #         "https://en.wikipedia.org/wiki/Tartar_sauce"
    #       ]
    #     },
    #     {
    #       "error_phrase": "The word Tartar is a Turkic word. It is believed to be named after the Tatar people.",
    #       "error_short_summary": "Etymology oversimplified/misleading",
    #       "why_wrong": "- The sauce name comes from French “sauce tartare”; “Tartar sauce” is attested in English from 1855.\n- “Tartar” (for the people) is a Western exonym via Medieval Latin/French, influenced by Latin “Tartarus”; the native ethnonym is “Tatar” (a Turkic people). “Tartar” itself is not a Turkic word.\n- Some sources connect “tartare” to the Tatars indirectly, but reputable culinary histories note the link is uncertain/folkloric.",
    #       "suggested_fix": "Replace with: “The name comes from French ‘sauce tartare’. The term ultimately relates to the Tatars (a Turkic people), but the English form ‘tartar’ is a Western exonym via Latin/French, not itself a Turkic word.”",
    #       "references": [
    #         "https://www.etymonline.com/word/tartar",
    #         "https://www.etymonline.com/word/Tatar",
    #         "https://en.wikipedia.org/wiki/Tatars#Etymology",
    #         "https://en.wikipedia.org/wiki/Tartar_sauce",
    #         "https://www.newyorker.com/culture/kitchen-notes/how-to-make-a-classic-bistro-style-steak-tartare-at-home"
    #       ]
    #     }
    #   ]
    # }


def main() -> None:
    url = "https://simple.wikipedia.org/wiki/Tartar_sauce"
    start_time = time.perf_counter()
    analysis = find_wikipedia_errors_advanced_2(url)
    total_time = time.perf_counter() - start_time
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
# error_short_summary: Wrong regional name (missing the word “sauce”)
# why_wrong: - In UK/Australian usage, the condiment is called “tartare sauce,” not just “tartare.”
# - Major dictionaries label the UK form as “tartare sauce.”
# - UK/Australian retail packaging likewise uses “Tartare Sauce.”
# suggested_fix: Change to: “Tartar sauce (called tartare sauce in the United Kingdom and Australia) …”
# references: ['https://dictionary.cambridge.org/dictionary/english/tartar-sauce', 'https://www.britannica.com/dictionary/tartar-sauce', 'https://www.tesco.com/groceries/en-GB/products/264876866', 'https://www.woolworths.com.au/Shop/ProductDetails/32766/masterfoods-seafood-sauce-tartare']
# --------------------------------------------------------------------------------
# error_phrase: The word Tartar is a Turkic word. It is believed to be named after the Tatar people.
# error_short_summary: Etymology misrepresented
# why_wrong: - The sauce name comes from French “sauce tartare.”
# - “Tartar” (as a people-name in Western languages) arrived via Medieval Latin and was influenced by Latin “Tartarus”; it is not itself a Turkic-language word. The Turkic ethnonym is “Tatar.”
# - The condiment’s name ultimately references the Tatars (a Turkic people), but the wording should reflect the French culinary term and the Tatar ethnonym accurately.
# suggested_fix: Replace with: “The name comes from the French sauce tartare and ultimately refers to the Tatars (a Turkic people). ‘Tartar’ is the Western form of ‘Tatar,’ influenced by Medieval Latin Tartarus.”
# references: ['https://www.merriam-webster.com/dictionary/tartar%20sauce', 'https://www.etymonline.com/word/tartar', 'https://www.britannica.com/topic/Tatar']
# --------------------------------------------------------------------------------
# Request duration: 235.90 seconds