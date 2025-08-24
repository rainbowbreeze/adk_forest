from google.adk.agents import Agent
from google.adk.tools import url_context



root_agent = Agent(
    # Has to be the same of the folder name
    name = "house_assistant_agent",
    model = "gemini-2.0-flash",
    description = "Agent to parse the url of a page specified by the user and returns a summary of the most important information present in the page",
    instruction = """
        You are an high skilled content reviewer.

        Please parse the url of a page specified by the user and returns a summary of the most important information present in the page.
        Present the summary in a clear and organized manner, perhaps using bullet points or numbered lists for individual stories, and a brief introductory sentence. Prioritize accuracy and neutrality in your summaries.

        If the page is about an house announcement, return a json with the following fields:
        - location_of_the_house
        - price_of_the_house
        - size_of_the_house
        - description_of_the_house
        
        Use url_context tool to get the content of the page.
        Format your output using markdown.
    """,
    tools = [url_context]
)

# Within house_assistant folder, run with ```adk web```, or ```adk run house_assistant_agent```
# URL
# - https://www.immobiliare.it/annunci/119836710/
# - https://www.immobiliare.it/annunci/121805074/
# - 