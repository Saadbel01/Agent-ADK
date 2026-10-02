"""
Geography Assistant Agent
Demonstrates ADK's tools parameter with a simple custom function tool.
Reference: https://google.github.io/adk-docs/agents/llm-agents#tools

"""


from google.adk.agents import LlmAgent

# Step 1: Define a tool function


def get_capital_city(country: str) -> str:

    """Retrieves the capital city for a specified country.

    Args:
    country (str): The name of the country.

    Returns:
    str: The capital city name or error message.

    """

    # Simulated capital city database

    capitals = {
        "france": "Paris",
        "japan": "Tokyo",
        "canada": "Ottawa",
        "germany": "Berlin",
        "brazil": "Brasília",
        "australia": "Canberra",
        "india": "New Delhi",
        "mexico": "Mexico City"
    }

    # Look up the capital
    return capitals.get(country.lower(), "Sorry, I don't have information"
                        f" about the capital of {country}.")
