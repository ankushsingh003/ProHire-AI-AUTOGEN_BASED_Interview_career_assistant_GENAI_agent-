import pytest



def test_planner_agent():
    planner_agent = get_planner_agent()
    assert planner_agent.name == "travel_agent"
    assert planner_agent.description == "Planner for the {job_position} position"
    assert planner_agent.input_func == input
    assert planner_agent.model == get_model_client()
    assert planner_agent.system_message == "You are a planner for the {job_position} position"
    assert planner_agent.termination_condition == get_terminate_condition()
    assert planner_agent.max_round == MAX_ROUND
    assert planner_agent.max_turn == MAX_TURN
    assert planner_agent.max_tokens == MAX_TOKENS
    