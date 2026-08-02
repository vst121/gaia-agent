from smolagents import tool
from ddgs import DDGS


@tool
def search_web(query: str) -> str:
    """
    Search the internet for current information.

    Args:
        query: The search phrase or question to look up online.

    Returns:
        A list of relevant search results.
    """

    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append(
                f"{r['title']}\n{r['body']}\n{r['href']}"
            )

    return "\n\n".join(results)