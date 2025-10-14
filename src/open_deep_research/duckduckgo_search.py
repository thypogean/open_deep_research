from langchain.tools import tool
from duckduckgo_search import DDGS


@tool("duckduckgo_search", return_direct=False)
def duckduckgo_search(query: str) -> str:
    """Search using DuckDuckGo and return summarized results."""
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=10)
    return "\n".join([f"{r['title']}: {r['href']}\n{r['body']}" for r in results])
