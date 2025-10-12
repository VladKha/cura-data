import time

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI


def find_wikipedia_errors(
    url: str,
    model: str = "gpt-5",
    reasoning_effort: str = "high",
) -> str:
    client = OpenAI()
    response = client.responses.create(
        model=model,
        reasoning={"effort": reasoning_effort},
        tools=[{"type": "web_search"}],
        input=f"""
Find at least one error on this Wikipedia page:
Wikipedia page: {url}
""",
    )
    return response.output_text

def main():
    url = "https://simple.wikipedia.org/wiki/Tartar_sauce"
    start = time.perf_counter()
    output_text = find_wikipedia_errors(url)
    total_time = time.perf_counter() - start
    print(output_text)
    print(f"Request duration: {total_time:.2f} seconds")


if __name__ == "__main__":
    main()
# Here are two clear errors on that page and how to fix them:
#
# - What the page says: “Tartar sauce (tartare in the United Kingdom and Australia) …” This is wrong because in British/Australian usage the term is tartare sauce (the word “sauce” is part of the name), not simply “tartare.” Authoritative dictionaries list the British form as “tartare sauce.” Fix: “Tartar sauce (called tartare sauce in the UK and Australia) …”. ([simple.wikipedia.org](https://simple.wikipedia.org/wiki/Tartar_sauce))
#
# - What the page says: “The word Tartar is a Turkic word. It is believed to be named after the Tatar people.” This conflates two things. Tatar is the Turkic ethnonym; Tartar is the Western/Latinized form influenced by association with Tartarus. The sauce name itself comes via French sauce tartare. Fix: “The name comes from French sauce tartare and ultimately refers to the Tatars (a Turkic people); the English form ‘Tartar’ is a Western variant of ‘Tatar’ influenced by Latin Tartarus.” ([simple.wikipedia.org](https://simple.wikipedia.org/wiki/Tartar_sauce))
#
# If you’d like, I can draft the exact replacement sentences you can paste into the article.
# Request duration: 162.36 seconds