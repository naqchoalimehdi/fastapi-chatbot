from fastapi import FastAPI
from pydantic import BaseModel
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os 

# Load environment variables
load_dotenv()

# Initialize the model
# Initialize Groq LLM
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
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
