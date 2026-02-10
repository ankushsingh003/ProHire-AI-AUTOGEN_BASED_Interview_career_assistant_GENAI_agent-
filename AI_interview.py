# from autogen_agentchat.agent import Agent
from autogen import UserProxyAgent, AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import os
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination   
from dotenv import load_dotenv 
from autogen_agentchat.ui import Console
from autogen_agentchat.base import TaskResult

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")



async def team_config(job_position = "software engineer"):
    
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
        api_key = os.getenv("OPENAI_API_KEY")
    )

    interviewer_agent = AssistantAgent(
        name="Interviewer",
        model=model_client,
        system_message='''
        You are a strict and professional interviewer. Your goal is to conduct a technical interview for the role of a {job_position} position .
        
        1. **Role**: You are interviewing a candidate for a {job_position} position.
        2. **Tone**: Professional, strict, and evaluative. Do not be overly friendly.
        3. **Behavior**:
            - Ask deep, technical questions.
            - Challenge the candidate's assumptions.
            - If the candidate gives a vague answer, ask for clarification or a specific example.
            - Do not reveal the answers to the questions.
            - Do not provide hints unless explicitly asked.
        4. **Question Style**:
            - Start with foundational concepts (e.g., "Explain the bias-variance tradeoff").
            - Move to practical implementation details (e.g., "How would you handle imbalanced data in a production setting?").
            - Include system design questions (e.g., "Design a recommendation system for a streaming service").
        5. **Interaction**:
            - Wait for the candidate to finish their answer before asking the next question.
            - Keep track of the time (mentally). If the candidate is taking too long on one question, move them along.
            - End the interview after 5-7 questions or when you feel you have enough information.
        6. **Output Format**:
            - Clearly state the question number.
            - Ask the question.
            - Wait for the response.
        7. **Termination**:
            - End the interview after 5-7 questions or when you feel you have enough information.
            - End the interview with the word "TERMINATE".

        '''
    )

    interviewee_agent = UserProxyAgent(
        name="Interviewee",
        input_func = input,
        description = "Candidate for the {job_position} position"

    )

    career_counsellor_agent = AssistantAgent(
        name="Career Counsellor",
        model=model_client,
        system_message='''
        You are a career counsellor. Your goal is to provide career advice to the candidate for {job_position} position.
        1. **Role**: You are a career counsellor.
        2. **Tone**: Professional, friendly, and encouraging.
        3. **Behavior**:
            - Listen to the candidate's concerns.
            - Provide practical advice.
            - Be supportive.
        4. **Interaction**:
            - Wait for the candidate to finish their response before providing advice.
            - End the session when you feel you have provided enough advice.
        5. **Output Format**:
            - Clearly state your advice.
            - Wait for the response.
        '''
    )

    terminate_condition = TextMentionTermination( text = "TERMINATE")

    team = RoundRobinGroupChat(
        participants = [interviewer_agent, interviewee_agent, career_counsellor_agent],
        max_round = 5,
        termination_condition = terminate_condition,
        max_tokens = 1000
    )
    return team

    # stream = team.run_stream( task = "conducting an interview for the position of software developer")

async def interview(stream):
    async for message in team.run_stream( task = "start the interview with the first question"):
        if isinstance( message , TaskResult):
            message: f"interview completed with result : {message.stop_reason}"

        else:
            message: f"{message.source} : {message.content}"
        
        yield message
            


async def main():
    job_position = "software engineer"

    team = await team_config(job_position)
    async for message in interview(team):
        print(message)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

