# Import FastAPI framework
from fastapi import FastAPI

# Import CORS middleware - allows Next.js frontend to talk to backend
from fastapi.middleware.cors import CORSMiddleware

# Import the data shapes we defined in models.py
from models import ChatRequest, ChatResponse

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
# FastAPI automatically validates the request body against ChatRequest
# and the return value against ChatResponse
@app.post("/chat")
def chat(request: ChatRequest) -> ChatResponse:
    # Hardcoded response for now - will be replaced with a real agent call
    return ChatResponse(response="it works", in_scope=True)