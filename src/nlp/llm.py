# external imports
from langchain_anthropic.chat_models import ChatAnthropic
from pydantic import ConfigDict

# internal imports


class LLMAnthropic(ChatAnthropic):
    """LLM for Chat."""

    class Config:
        """Configuration for this pydantic object."""

        model_config: ConfigDict = ConfigDict(extra="allow")

    def __init__(
        self: "LLMAnthropic",
        model_name: str = "claude-3-haiku-20240307",
        **kwargs: dict,
    ) -> None:
        """Initialize LLM.

        Args:
        ----
            model_name (str): model id of anthropic llm
            **kwargs (dict): additional arguments

        """
        from config import Settings, get_settings

        settings: Settings = get_settings()

        super().__init__(
            model_name=model_name,
            timeout=None,
            stop=None,
            api_key=settings.ANTHROPIC_API_KEY,
            **kwargs,
        )
