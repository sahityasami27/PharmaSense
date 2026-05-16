from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

load_dotenv()

langsmith_key = os.getenv("LANGCHAIN_API_KEY")

if langsmith_key:
    os.environ["LANGCHAIN_API_KEY"] = langsmith_key
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "PharmaSense"

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)