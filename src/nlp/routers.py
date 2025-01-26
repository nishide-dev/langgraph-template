# external imports
from langgraph.graph import END

# internal imports
from .types import AgentState


def route_tools(
    state: AgentState,
) -> str:
    """Use in the conditional_edge to route to the ToolNode if the last message has tool calls. Otherwise, route to the end.

    Args:
    ----
        state (AgentState): agent state

    Returns:
    -------
        node (str): node

    """  # noqa: E501
    if isinstance(state, list):
        ai_message = state[-1]
    elif state.messages:
        ai_message = state.messages[-1]
    else:
        value_error = f"No message found in input state to tool_edge: {state}"
        raise ValueError(value_error)
    if hasattr(ai_message, "tool_calls") and len(ai_message.tool_calls) > 0:
        return "tools"
    return END
