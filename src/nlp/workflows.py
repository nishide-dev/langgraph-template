# external imports
from langchain_core.tools import BaseTool
from langgraph.graph import StateGraph
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import ToolNode, tools_condition

# internal imports
from .llm import LLMAnthropic
from .nodes import ChatbotNode
from .types import AgentState


def chatbot_workflow(llm: LLMAnthropic, tools: list[BaseTool]) -> CompiledStateGraph:
    """Chatbot Workflow.

    Args:
    ----
        llm (LLMAnthropic): llm
        tools (list[BaseTool]): tools

    Returns:
    -------
        graph (CompiledStateGraph): compiled graph

    """
    tool_node = ToolNode(tools)

    workflow = StateGraph(AgentState)
    workflow.add_node("chatbot", ChatbotNode(llm))
    workflow.add_node("tools", tool_node)
    workflow.add_conditional_edges(
        "chatbot",
        tools_condition,
    )
    workflow.add_edge("tools", "chatbot")
    workflow.set_entry_point("chatbot")
    return workflow.compile()
