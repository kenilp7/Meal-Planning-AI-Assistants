from autogen_core.tools import FunctionTool

def budget_checker_tool(cost: float, current_budget: float) -> dict:
    """
    Check if a given cost fits within the current budget.

    :param cost: float, the cost to check.
    :param current_budget: float, the current remaining budget.
    :return: dict, containing whether the cost fits the budget and a message.
    """
    if cost > current_budget:
        return {
            "fits_budget": False,
            "message": f"This exceeds your budget by ${cost - current_budget:.2f}."
        }
    return {
        "fits_budget": True,
        "message": f"The cost of ${cost:.2f} fits within your budget."
    }

budget_checker_tool = FunctionTool(budget_checker_tool, description="Check if a given cost fits within the budget.")
