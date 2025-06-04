from langchain_google_genai import GoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from dotenv import dotenv_values


config = dotenv_values(".env")

def get_weather():

weather_agent = create_react_agent(GoogleGenerativeAI(api_key=config["GEMINI_API_KEY"]))
