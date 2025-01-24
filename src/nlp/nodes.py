# external imports

# internal imports
from .llm import LLMAnthropic
from .types import AgentState


class ChatbotNode:
    """Chatbot Node class."""

    def __init__(self: "ChatbotNode", llm: LLMAnthropic) -> None:
        """Initialize ChatbotNode.

        Args:
        ----
            llm (LLMAnthropic): llm

        """
        self.llm = llm

    def __call__(self: "ChatbotNode", state: AgentState) -> dict:
        """Process messages using the LLM.

        Args:
        ----
            state (AgentState): agent state

        Returns:
        -------
            messages (dict): messages

        """
        return {"messages": self.llm.invoke(state.messages)}
