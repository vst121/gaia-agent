from smolagents import tool


@tool
def calculator(expression: str) -> str:
    """
    Evaluate mathematical expressions.

    Args:
        expression: The mathematical expression to evaluate, for example "25 * 4" or "(100 / 5) + 10".

    Returns:
        The calculated result as a string.
    """

    try:
        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"Calculation error: {e}"