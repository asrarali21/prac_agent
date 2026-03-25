from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
import os


GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
class LeadAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            api_key=GOOGLE_API_KEY
        )
    def build_prompt(self, user_query: str, plan: str):
        system_prompt = f"""
You are a Lead Agent in an AI agent system. Your responsibility is to coordinate the workflow to answer the user's request effectively.

Analyze the following user query:
{user_query}

Execution plan from planner agent:
{plan}

Your specific tasks are:
1. Understand the user's intent and the complexity of the request.
2. Use the provided plan to produce a clear final response.
3. If needed, refine the plan into concise actionable guidance.
4. Maintain a professional and helpful tone.

Provide only the final response to the user.
        """
        return [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_query),
        ]

    async def lead(self, user_query: str, plan: str):
        response = await self.llm.ainvoke(self.build_prompt(user_query, plan))
        return response.content
