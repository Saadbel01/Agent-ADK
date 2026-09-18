import asyncio

from .agent import root_agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai.types import Content, Part


async def main():
    # Setup session and runner
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="my_app",
        user_id="user_1",
        session_id="test_session")

    runner = Runner(
        app_name="my_app",
        agent=root_agent,
        session_service=session_service)

    user_message = Content(
        parts=[Part(text="Hi, my name is Saad.")])

    print("=== Running agent ===")
    result = runner.run(
        user_id="user_1",
        session_id="test_session",
        new_message=user_message
    )

    # Show final response
    for event in result:
        if event.is_final_response() and event.content and event.content.parts:
            print(f"\nAgent response: {event.content.parts[0].text}")

    # Access state programmatically
    print("\n=== State after execution ===")
    print(f"Full state: {session.state}")
    print(f"Extracted name: {session.state.get('user_name')}")

    if session.state.get("user_name"):
        print("Name was successfully extracted and stored!")
    else:
        print("Name extraction failed.")


if __name__ == "__main__":
    asyncio.run(main())
