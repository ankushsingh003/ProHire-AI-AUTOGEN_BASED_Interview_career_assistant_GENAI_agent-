from AI_interview import team_config, interview 
import asyncio
from autogen_agentchat.messages import TextMessage
from teams.travel_team import get_travel_team

team = get_travel_team()

async def main():
    job_position = "software engineer"
    task = TextMessage(
        content = "start the interview with the first question",
        source = "user"
    )
    result = await team.run(task =task)
    for message in result:
        print(message)

if __name__ == "__main__":
    asyncio.run(main())



