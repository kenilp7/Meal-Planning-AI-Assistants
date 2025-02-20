import asyncio
from src.team import team
from autogen_agentchat.ui import Console

async def main():
    """Running the interactive meal planning assistant."""
    user_input = input("Enter your budget for meals today: ")
    stream = team.run_stream(task=user_input)  
    await Console(stream)  

if __name__ == "__main__":  
    asyncio.run(main())
