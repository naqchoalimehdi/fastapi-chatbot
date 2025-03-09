from fastapi import FastAPI
from pydantic import BaseModel
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os 

# Load environment variables
load_dotenv()

# Initialize the model
llm = ChatGroq(
    api_key="gsk_0da2rsfsOvURR04xaA39WGdyb3FYfpGE8WaTZOe2uJL6oPITAeI1gsk_ZbTz0msdoRqW7aPrZKlcWGdyb3FYUsmcJVmP4UIdnZ0Q8NUcix5O",  # Replace with actual key
    model="llama-3.3-70b-versatile",
    temperature=0.0,
    max_retries=2,
)

# FastAPI app
app = FastAPI()

# Request Model
class ChatRequest(BaseModel):
    topic: str

@app.get("/")
def home():
    return {"message": "FastAPI app deployed on Vercel!"}

# Chat with the LLM
@app.post("/chat")
async def chat(request: ChatRequest):
    prompt = f"You are a helpful assistant. Write something about {request.topic}"
    response = llm.invoke(prompt)  # Corrected to invoke()
    return {"response": response}  # No `.content`, return response directly
