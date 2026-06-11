import anthropic
from dotenv import load_dotenv
import os 
load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
def ask_ai(question):
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return message.content[0].text

print("AI Engineer Assiatant Ready!")
print("Type 'quit' to exit\n")

while True:
    question = input("Ask the AI anything: ")
    if question.lower() == "quit":
        break
    response = ask_ai(question)
    print(f"\nAI: {response}\n")