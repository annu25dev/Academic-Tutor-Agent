import os
from dotenv import load_dotenv
from crewai import LLM
load_dotenv()
llm = LLM(

    model="gemini/gemini-2.5-flash",

    api_key=os.getenv("GEMINI_API_KEY"),

    temperature=0.3

)
