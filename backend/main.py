# Import FastAPI framework
from fastapi import FastAPI

# Import CORS middleware - allows Next.js frontend to talk to backend
from fastapi.middleware.cors import CORSMiddleware

# Import the data shapes we defined in models.py
from models import ChatRequest, ChatResponse

from agent import run_agent

# Create the FastAPI app instance
app = FastAPI()

# Add CORS middleware to the app
# allow_origins=["*"] means any frontend can talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the /chat endpoint, accepts POST requests
@app.post("/query")
def chat(request: ChatRequest) -> ChatResponse:
    result = run_agent(request.message)
    return ChatResponse(response=result["response"], in_scope=result["in_scope"])