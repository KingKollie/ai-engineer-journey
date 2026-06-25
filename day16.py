from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# A simple model for our request
class QuestionRequest(BaseModel):
    question: str
    document: str

# Root endpoint - tests if the API is alive
@app.get("/")
def home():
    return {"message": "Kollie's AI API is running!"}

# Health check endpoint
@app.get("/health")
def health():
    return {"status": "healthy"}

# Q&A endpoint
@app.post("/ask")
def ask_question(request: QuestionRequest):
    import anthropic
    from dotenv import load_dotenv
    import os
   
    load_dotenv()
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
   
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"Document:\n{request.document}\n\nQuestion: {request.question}"
            }
        ]
    )
   
    return {
        "question": request.question,
        "answer": message.content[0].text
    }
