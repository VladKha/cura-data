import time

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
    
analysis_prompt = """
You are an expert in detecting errors and inconsistencies in data.
You will be provided with a Wikipedia URL.
Your goal will be to find at least one error on the page and provide response with corresponding analysis.
"""

url = "https://simple.wikipedia.org/wiki/Tartar_sauce"
start_time = time.perf_counter()
client = instructor.from_provider("openai/gpt-5", mode=instructor.Mode.RESPONSES_TOOLS_WITH_INBUILT_TOOLS)
data_error_analysis = client.responses.create(
    # model="gpt-5", # gpt-5 | gpt-5-nano
    reasoning={"effort": "high"}, # high | low
    tools=[{"type": "web_search"}],
    input=[
        {"role": "system", "content": analysis_prompt},
        {"role": "user", "content": f"Wikipedia URL: {url}"},
    ],
    response_model=DataErrorAnalysis
)
elapsed = time.perf_counter() - start_time
for data_error in data_error_analysis.errors:
    print("error_phrase:", data_error.error_phrase)
    print("error_short_summary:", data_error.error_short_summary)
    print("why_wrong:", data_error.why_wrong)
    print("suggested_fix:", data_error.suggested_fix)
    print("references:", data_error.references)
    print("-" * 80)
print(f"Request duration: {elapsed:.2f} seconds")
