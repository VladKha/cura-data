import time

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

url = "https://simple.wikipedia.org/wiki/Tartar_sauce"
# https://en.wikipedia.org/wiki/Reese's_Pieces
start_time = time.perf_counter()
client = OpenAI()
response = client.responses.create(
    model="gpt-5",
    reasoning={"effort": "high"},
    tools=[{"type": "web_search"}],
    input=f"""
Find at least one error on this Wikipedia page:
Wikipedia page: {url}
"""
)
elapsed = time.perf_counter() - start_time

print(response.output_text)
print(f"Request duration: {elapsed:.2f} seconds")
