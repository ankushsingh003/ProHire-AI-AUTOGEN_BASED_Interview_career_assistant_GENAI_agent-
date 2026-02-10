from autogen_agentchat.conditions import TextMentionTermination
import json
from config.settings import TERMINATE_MESSAGE

terminate_condition = TextMentionTermination( text = TERMINATE_MESSAGE)



def save_chat_history( agent , filename):
    state = agent.save_state()
    with open(filename , 'w') as f:
        json.dump(state , f , indent = 4)


def load_chat_history( agent , filename):
    with open(filename , 'r') as f:
        state = json.load(f)
    agent.load_state(state)
    return agent



def get_terminate_condition():
    return terminate_condition