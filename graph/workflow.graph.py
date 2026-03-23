from langgraph.graph import StateGraph , START , END
from typing import TypedDict
from agents.planner_agent import PlanningAgent

class Agentstate(TypedDict):
    user_query = str
    planner_agent =str
    lead_agent = str
def build_agent_graph():
    planner = PlanningAgent()
    graph = StateGraph(Agentstate)

    graph.add_node("planner_agent" , planner.plan)

