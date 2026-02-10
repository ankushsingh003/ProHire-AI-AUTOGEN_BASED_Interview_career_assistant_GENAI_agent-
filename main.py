
from AI_interview import team_config, interview 
import asyncio



async def main():
    job_position = "software engineer"

    team = await team_config(job_position)
    async for message in interview(team):
        print( "-" * 100)
        print(message)

if __name__ == "__main__":
    asyncio.run(main())



