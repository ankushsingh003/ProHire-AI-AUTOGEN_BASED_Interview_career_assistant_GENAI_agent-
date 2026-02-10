from autogen_agentchat.agents import UserProxyAgent






def get_interviewee_agent():
    interviewee_agent = UserProxyAgent(
        name="Interviewee",
        input_func = input,
        description = "Candidate for the {job_position} position"

    )
    return interviewee_agent
    