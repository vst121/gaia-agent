from smolagents import tool
from ddgs import DDGS


@tool
def web_search(query: str) -> str:
    """
    Search the web for information.

    Args:
        query: The search query to look up.

    Returns:
        Search results as text.
    """
    
    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append(
                f"{r['title']}\n{r['body']}\n{r['href']}"
            )

    return "\n\n".join(results)