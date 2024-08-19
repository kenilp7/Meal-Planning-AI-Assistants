from autogen_agentchat.agents import AssistantAgent
from .model_client import model_client
from .tools import budget_checker_tool

budget_agent = AssistantAgent(
    name="BudgetAssistant", 
    tools=[budget_checker_tool], 
    model_client=model_client,
    description="Assists in managing budget constraints.",
    system_message="Ensure that all expenses for the day fit within the given budget. Update budget after each meal plan."
)

breakfast_agent = AssistantAgent(
    name="BreakfastPlanner", model_client=model_client,
    description="Suggests breakfast plans based on dietary preferences. Dont use up all budget. Check the remaining budget and pass on budget to other planners.",
    system_message="Generate a breakfast plan for the day within the given budget."
)

lunch_agent = AssistantAgent(
    name="LunchPlanner", model_client=model_client,
    description="Suggests lunch plans.",
    system_message="Provide lunch options within budget and nutrition guidelines. Also check the remaining budget and keep budget for other planners."
)

dinner_agent = AssistantAgent(
    name="DinnerPlanner", model_client=model_client,
    description="Suggests dinner plans.",
    system_message="Generate dinner meal plans for the day keeping budget constraints in mind."
)

snack_agent = AssistantAgent(
    name="SnackPlanner", model_client=model_client,
    description="Suggests snack ideas.",
    system_message="Provide snack suggestions that fit within the budget for the day."
)
