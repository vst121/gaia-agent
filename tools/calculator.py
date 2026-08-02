from smolagents import tool


@tool
def calculator(expression: str) -> str:
    """
    Evaluate mathematical expressions.

    Args:
        expression: A mathematical expression such as 25*4.

    Returns:
        The calculated result.
    """
    
    try:
        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"Calculation error: {e}"