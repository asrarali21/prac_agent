
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage , HumanMessage

import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("Error: GOOGLE_API_KEY environment variable not found")


class PlanningAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            api_key=GOOGLE_API_KEY
        )

    def build_prompt(self , user_query:str):
        system_prompt =  f"""
        You are an AI Planning Agent.
        Your role is to break down complex user goals into clear,
logical, and executable steps.

Rules:
- Do not perform the task
- Only generate a plan
- Steps must be ordered
- Steps must be actionable
- Max 8 steps

        """
        return [SystemMessage(content = system_prompt), HumanMessage(content=user_query)]
    
    async def plan(self , user_query:str):

        response = await self.llm.ainvoke(self.build_prompt(user_query=user_query))

        return response.content


        