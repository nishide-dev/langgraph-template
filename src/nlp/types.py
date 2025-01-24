# external imports
from typing import Annotated

from langgraph.graph.message import add_messages
from pydantic import BaseModel

# internal imports


class AgentState(BaseModel):
    """Agent state."""

    messages: Annotated[list, add_messages]
