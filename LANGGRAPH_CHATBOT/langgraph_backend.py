from langgraph.graph import StateGraph,END,START
from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from langchain_mistralai import ChatMistralAI
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv

load_dotenv()

checkpointer = MemorySaver()

llm = ChatMistralAI(model="ministral-3b-latest", temperature=0.7)

class ChatState(TypedDict):
   messages: Annotated[list[BaseMessage], add_messages]
   
def chat_node(state:ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages":[response]}

graph = StateGraph(ChatState)
graph.add_node("chat_node" ,chat_node)
graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

chatbot = graph.compile(checkpointer=checkpointer)


