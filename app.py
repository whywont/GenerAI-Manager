import config
from config import TAVILY_API_KEY, OPENAI_API_KEY
from langgraph.graph import Graph
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import PromptTemplate
from langgraph.prebuilt import ToolExecutor
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, StateGraph, START
import operator
from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, AIMessage

memory = SqliteSaver.from_conn_string(":memory:")

# Rest of your code

class State(TypedDict):
  messages: Annotated[list, add_messages]

# def chatbot(state: State, llm):
#     return {"messages": [llm.invoke(state["messages"])]}

def create_llm():

  tools = [TavilySearchResults(max_results=10)]
  tool_executor = ToolExecutor(tools)
  model = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0)
  # model = model.bind_tools(tools)

  return model, tool_executor

class State(TypedDict):
  messages: Annotated[list, add_messages]

def chatbot(state: State):
  llm, te = create_llm()
  messages = state["messages"]
  response = llm.invoke(messages)
  return {"messages": [AIMessage(content=response.content)]}

def main():
    workflow = StateGraph(State)
    workflow.add_node("chatbot", chatbot)
    workflow.set_entry_point("chatbot")
    
    app = workflow.compile()

    # Initialize the conversation
    conversation_state = {"messages": []}

    print("Welcome to the chatbot! Type 'quit' to exit.")

    while True:
      user_input = input("You: ")
      
      if user_input.lower() == 'quit':
        print("Goodbye!")
        break

      # Add the user's message to the conversation state
      conversation_state["messages"].append(HumanMessage(content=user_input))

      # Run the graph with the updated state
      final_state = app.invoke(conversation_state)

      # Update the conversation state with the new messages
      conversation_state = final_state

      # Print the AI's response
      ai_response = conversation_state["messages"][-1].content
      print("AI:", ai_response)

  


if __name__ == "__main__":
  main()