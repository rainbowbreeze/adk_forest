"""Basic agent using Ollama local
Inspiration from https://www.youtube.com/watch?v=B5x6asWzTNU

https://www.youtube.com/watch?v=TFjKTJJWi78
* Useful to set OS env vars to control ollama directly into the code
"""
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import litellm

litellm._turn_on_debug()

# It's needed at least a root_agent
root_agent = Agent(
    name = "ollama_greeting_agent",
    # Uses a more spartan response
    # model = LiteLlm(model="ollama/gemma3:4b"),
    # Uses a nicer response
    model = LiteLlm(model="ollama_chat/gemma3:4b"),
    description = "Agent to greet people in new and original ways",
    instruction = """
    Find an original and fresh way to greeting a person.
    Use no more than one sentence and the attitute should be positive and welcoming
    """
)

# Run with adk-web, or adk run greeting_agent