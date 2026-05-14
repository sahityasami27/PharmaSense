from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("API Key Loaded:", bool(api_key))

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=api_key,
    temperature=0.3
)

response = llm.invoke("Say hello and confirm the API is working.")

print(response.content)