from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from config.settings import TERMINATE_MESSAGE , MAX_ROUND , MAX_TURN , MAX_TOKENS
from agents.interviewer_agent import get_interviewer_agent
from agents.interviewee_agent import get_interviewee_agent
from agents.career_counsellor_agent import get_career_counsellor_agent
from utils.utils import get_terminate_condition




def get_travel_team():
    team = RoundRobinGroupChat(
        participants = [get_interviewer_agent(), get_interviewee_agent(), get_career_counsellor_agent()],
        max_round = MAX_ROUND,
        termination_condition = get_terminate_condition(),
        max_tokens = MAX_TOKENS
    )
    return team
    