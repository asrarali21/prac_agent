from fastapi import FastAPI
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage , HumanMessage
import os
from dotenv import load_dotenv
from agents.planner_agent import PlanningAgent


load_dotenv()



app = FastAPI()





class UserQuery(BaseModel):
    user_query : str





@app.post("/")
async def handle_user_query(user_query:UserQuery):
    print("user_query : ", user_query)

    planner_agent = PlanningAgent()

    response = await planner_agent.plan(user_query)

    return response









