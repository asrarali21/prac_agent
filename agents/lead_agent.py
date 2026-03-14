from langchain_google_genai import ChatGoogleGenerativeAI

import os


GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
class LeadAgent:
    def __init__(self):
        self.llms = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            api_key=GOOGLE_API_KEY
        )

    def build_prompt(self , user_query )