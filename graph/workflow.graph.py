from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from agents.planner_agent import PlanningAgent
from agents.lead_agent import LeadAgent


class AgentState(TypedDict, total=False):
    user_query: str
    plan: str
    final_response: str


def build_agent_graph():
    planner = PlanningAgent()
    lead = LeadAgent()
    graph = StateGraph(AgentState)

    async def planner_node(state: AgentState) -> AgentState:
        plan = await planner.plan(state["user_query"])
        return {"plan": plan}

    async def lead_node(state: AgentState) -> AgentState:
        final_response = await lead.lead(state["user_query"], state["plan"])
        return {"final_response": final_response}

    graph.add_node("planner_agent", planner_node)
    graph.add_node("lead_agent", lead_node)

    graph.add_edge(START, "planner_agent")
    graph.add_edge("planner_agent", "lead_agent")
    graph.add_edge("lead_agent", END)

    return graph.compile()


