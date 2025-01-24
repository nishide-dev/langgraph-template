# external imports
import pytest

# internal imports
from src.nlp.llm import LLMAnthropic


@pytest.fixture()
def llm_anthropic() -> LLMAnthropic:
    return LLMAnthropic()


def test_invoke(llm_anthropic: LLMAnthropic) -> None:
    response = llm_anthropic.invoke("Hello")
    assert response is not None
    assert isinstance(response.content, str)
    assert len(response.content) > 0
