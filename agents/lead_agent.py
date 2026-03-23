from langchain_google_genai import ChatGoogleGenerativeAI

import os


GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
class LeadAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            api_key=GOOGLE_API_KEY
        )

    async def build_prompt(self , user_query ):
        system_prompt = """
You are a Lead Agent in an AI agent system. Your responsibility is to coordinate the workflow to answer the user's request effectively.

Analyze the following user query:
"{user_query}"

Your specific tasks are:
1. Understand the user's intent and the complexity of the request.
2. If the request requires multiple steps or specialized knowledge, break it down into logical sub-tasks.
3. If you can answer directly with general knowledge, provide the answer.
4. Maintain a professional and helpful tone.

Provide a clear and structured response outlining the execution plan or the final answer.
        """

    async def lead(self , user_query):
        response = await self.llm.ainvoke(self.build_prompt(user_query))

        return response.content
