import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("Anthropic_API_KEY"))
 
system_prompt = """You are a helpful document assistant.
you will be given the content of a document, and the user
will ask you questions about it. Only answer baased on the
document content provided if the answer isn't in the 
document, say so."""

def read_d0cunent(filename):
    with open(filename, "r") as f:
        return f.read()
    
def ask_about_doucment(document_text, question):
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": f"Document:\n{document_text}\n\nQuestion: {question}"
            }
        ]
    )
    return message.content[0].text

filename = input("Enter the filename to load: ")
document_text = read_d0cunent(filename)
print(f"\nLoaded {filename}! Ask me anything about it.\n")

while True:
    question = input("you: ")
    if question.lower() =="quit":
       print("see you next session!")
       break
    answer = ask_about_doucment(document_text, question)
    print(f"\nAI: {answer}\n")