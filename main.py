from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from agents.planner_agent import PlanningAgent


load_dotenv()



app = FastAPI()
planner_agent = PlanningAgent()





class UserQuery(BaseModel):
    user_query : str





@app.post("/")
async def handle_user_query(user_query:UserQuery):
    print("user_query : ", user_query)

    response = await planner_agent.plan(user_query.user_query)

    return response









