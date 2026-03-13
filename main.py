from fastapi import FastAPI
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv


load_dotenv()



app = FastAPI()



GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("Error: GOOGLE_API_KEY environment variable not found")


class UserQuery(BaseModel):
    user_query : str


class PlanningAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.1-pro-preview",
            api_key=GOOGLE_API_KEY
        )

    def build_prompt(self , user_query:str):
        return f"""
        You are an AI Planning Agent.
        Your role is to break down complex user goals into clear,
logical, and executable steps.

Rules:
- Do not perform the task
- Only generate a plan
- Steps must be ordered
- Steps must be actionable
- Max 8 steps

User query:
{user_query}

        """
    
    async def plan(self , user_query:str):

        response = await self.llm.ainvoke(self.build_prompt(user_query=user_query))

        return response.content


        


@app.post("/")
async def handle_user_query(user_query:UserQuery):
    print("user_query : ", user_query)

    planner_agent = PlanningAgent()

    response = await planner_agent.plan(user_query)

    return response









