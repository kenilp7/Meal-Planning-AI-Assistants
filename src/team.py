from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from .agents import budget_agent, breakfast_agent, lunch_agent, dinner_agent, snack_agent

termination = MaxMessageTermination(max_messages=10)

team = RoundRobinGroupChat(
    participants = [budget_agent, breakfast_agent, lunch_agent, dinner_agent, snack_agent],
    termination_condition = termination
)

