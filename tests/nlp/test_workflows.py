# external imports
import pytest
from langchain_core.tools import BaseTool

# internal imports
from src.nlp.llm import LLMAnthropic
from src.nlp.tools import TavilySearchResultsTool
from src.nlp.workflows import chatbot_workflow


@pytest.fixture()
def tools() -> list[BaseTool]:
    return [TavilySearchResultsTool()]


@pytest.fixture()
def llm_anthropic(tools: list[BaseTool]) -> LLMAnthropic:
    llm = LLMAnthropic()
    return llm.bind_tools(tools)


def test_chatbot_workflow(llm_anthropic: LLMAnthropic, tools: list[BaseTool]) -> None:
    graph = chatbot_workflow(llm_anthropic, tools)
    assert graph is not None
    print(graph.get_graph().draw_ascii())  # noqa: T201

    response = graph.invoke({"messages": [{"role": "user", "content": "Hello"}]})
    assert response is not None
    assert isinstance(response, dict)
    assert isinstance(response["messages"], list)
    assert len(response["messages"]) > 0
