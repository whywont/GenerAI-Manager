import config
from config import TAVILY_API_KEY, OPENAI_API_KEY
from langgraph.graph import Graph
from langchain_community.chat_models import ChatOpenAI


def create_llm():
  return ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0)


def main():
   print("Main")
  








if __name__ == "__main__":
    main()