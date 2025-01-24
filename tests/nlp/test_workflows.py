# external imports
import pytest

# internal imports
from src.nlp.llm import LLMAnthropic
from src.nlp.workflows import chatbot_workflow


@pytest.fixture()
def llm_anthropic() -> LLMAnthropic:
    return LLMAnthropic()


def test_chatbot_workflow(llm_anthropic: LLMAnthropic) -> None:
    workflow = chatbot_workflow(llm_anthropic)
    assert workflow is not None
    response = workflow.invoke({"messages": [{"role": "user", "content": "Hello"}]})
    assert response is not None
    assert isinstance(response, dict)
    assert isinstance(response["messages"], list)
    assert len(response["messages"]) > 0
