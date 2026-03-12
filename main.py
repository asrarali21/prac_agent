from fastapi import FastAPI
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI

app = FastAPI()




class UserQuery(BaseModel):
    user_query : str


class PlanningAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.1-pro-preview"
        )

    def build_prompt():
        return f"""
      You are a Speciliazed planner agent How plans all the things 
        """


@app.post("/")
def handle_user_query(user_query:UserQuery):
    print("user_query : ", user_query)




