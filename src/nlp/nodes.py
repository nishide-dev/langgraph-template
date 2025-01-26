# external imports
import json

from langchain_core.messages import ToolMessage
from langchain_core.tools import BaseTool

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
        return {"messages": [self.llm.invoke(state.messages)]}


class BasicToolNode:
    """A node that runs the tools requested in the last AIMessage."""

    def __init__(self: "BasicToolNode", tools: list[BaseTool]) -> None:
        """Initialize BasicToolNode.

        Args:
        ----
            tools (list[BaseTool]): tools

        """
        self.tools_by_name = {tool.name: tool for tool in tools}

    def __call__(self: "BasicToolNode", inputs: dict) -> dict:
        """Process messages using the LLM.

        Args:
        ----
            inputs (dict): inputs

        Returns:
        -------
            messages (dict): messages

        """
        if messages := inputs.get("messages", []):
            message = messages[-1]
        else:
            value_error = f"No message found in input: {inputs}"
            raise ValueError(value_error)
        outputs = []
        for tool_call in message.tool_calls:
            tool_result = self.tools_by_name[tool_call["name"]].invoke(
                tool_call["args"]
            )
            outputs.append(
                ToolMessage(
                    content=json.dumps(tool_result),
                    name=tool_call["name"],
                    tool_call_id=tool_call["id"],
                )
            )
        return {"messages": outputs}
