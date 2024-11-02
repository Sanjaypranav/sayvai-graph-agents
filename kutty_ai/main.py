import dotenv

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from kutty_ai.agents import KuttyAssistant, State
from kutty_ai.tools import call_sanjay_tool, call_subash_tool

dotenv.load_dotenv()
llm = ChatOpenAI(
    model="gpt-4o-mini",
)

def chatbot(state: State) ->  dict:
    return {"messages": llm.invoke(state["messages"])}

#tools 
tools = [
    
]

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

while True:
  user_input=input("User: ")
  if user_input.lower() in ["quit","q"]:
    print("Good Bye")
    break
  for event in graph.stream({'messages':("user",user_input)}):
    print(event.values())
    for value in event.values():
    #   print(value['messages'])
      print("Assistant:",value["messages"].content)
