# external imports
from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

# internal imports
from .llm import LLMAnthropic
from .nodes import ChatbotNode
from .types import AgentState


def chatbot_workflow(llm: LLMAnthropic) -> CompiledStateGraph:
    """Chatbot Workflow.

    Args:
    ----
        llm (LLMAnthropic): llm

    Returns:
    -------
        graph (CompiledStateGraph): compiled graph

    """
    workflow = StateGraph(AgentState)
    workflow.add_node("chatbot", ChatbotNode(llm))
    workflow.add_edge(START, "chatbot")
    workflow.add_edge("chatbot", END)
    return workflow.compile()
