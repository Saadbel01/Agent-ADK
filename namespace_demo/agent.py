"""

Namespace Demo - Shows all four state
namespaces

Demonstrates temp:, session, user:,
and app: persistence scopes.


Reference: https://google.github.io/
adk-docs/sessions/state.md

"""

from google.adk.agents import LlmAgent

# Create agent that uses all four namespaces

root_agent = LlmAgent(
    model="gemini-3.5-flash",
    name="namespace_demo",
    instruction="""
    You are a demo assistant showing state namespaces.

    === App State (global for all users)===

    App name: {app:name?NamespaceDemo}
    App version: {app:version?1.0}

    === User State (persists across sessions) ===
    User preference: {user:theme?notset}

    === Session State (persists this conversation) ===
    Conversation topic: {topic?notset}

    === Temp State (current turn only) ===

    Current step: {temp:step?not set}


    Respond with a friendly message
    showing these namespace values.

    """,
    output_key="resonse"
    )
