# external imports
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper

# internal imports
from config import get_settings


class TavilySearchResultsTool(TavilySearchResults):
    """TavilySearchResultsTool."""

    def __init__(self: "TavilySearchResultsTool", **kwargs: dict) -> None:
        """Initialize TavilySearchResultsTool."""
        settings = get_settings()

        kwargs["api_wrapper"] = TavilySearchAPIWrapper(
            tavily_api_key=settings.TAVILY_API_KEY
        )
        super().__init__(max_results=5, **kwargs)
