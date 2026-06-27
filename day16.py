from fastapi import FastAPI
from pydantic import BaseModel
from config import ANTHROPIC_API_KEY, MODEL_NAME, MAX_TOKENS
import anthropic

app = FastAPI()
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

class QuestionRequest(BaseModel):
    question: str
    document: str

@app.get("/")
def home():
    return {"message": "Kollie's AI API is running!"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/ask")
def ask_question(request: QuestionRequest):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=MAX_TOKENS,
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