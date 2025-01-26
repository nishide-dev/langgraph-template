# external imports
import sys
from pathlib import Path

from langgraph.graph.state import CompiledStateGraph

# internal imports
sys.path.append(str(Path(__file__).parent.parent))
from src.nlp.llm import LLMAnthropic
from src.nlp.tools import TavilySearchResultsTool
from src.nlp.workflows import chatbot_workflow


def stream_graph_updates(user_input: str, graph: CompiledStateGraph) -> None:
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)  # noqa: T201


# main
def main() -> None:
    llm = LLMAnthropic()
    tools = [TavilySearchResultsTool()]
    llm_with_tools = llm.bind_tools(tools)
    graph = chatbot_workflow(llm_with_tools, tools)

    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")  # noqa: T201
                break

            stream_graph_updates(user_input, graph)
        except:  # noqa: E722
            # fallback if input() is not available
            user_input = "What do you know about LangGraph?"
            print("User: " + user_input)  # noqa: T201
            stream_graph_updates(user_input, graph)
            break


if __name__ == "__main__":
    main()
