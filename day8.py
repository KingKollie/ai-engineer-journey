import anthropic 
from dotenv import load_dotenv
import os 

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

system_prompt = """You are a helpful document assistant.
you will be given the contents off multiple documents.
Answer questions based only on the provided documents.
When answering, mention which document the infromation came from.
If the answer isn't in any document, say so."""

def read_document(filename):
    with open(filename, "r") as f:
        return f.read()
    
def build_context(documents):
    context = ""
    for name, text in documents.items():
        context += f"--- Document: {name} ---\n{text}\n\n"
    return context

def ask_about_documents(context, question):
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        system=system_prompt,
        messages=[ 
            {
                "role": "user",
                "content": f"Documents:\n{context}\n\nQuestion: {question}"
            }

        ]
    )
    return message.content[0].text

# Load multiple documents
documents = {}
print("Enter filenames to load (type 'done' when finished):")

while True:
    filename = input("filename: ")
    if filename.lower() == "done":
        break
    if os.path.exists(filename):
        documents[filename] = read_document(filename)
        print(f" Loaded {filename}")
    else:
        print(f"x file not found: {filename}")

    if not documents:
        print("No documents loaded. Exiting. ")
    else:
        context = build_context(documents)
        print(f"\nLoaded {len(documents)} document(s). Ask me anything!\n")

        while True:
            question = input("You: ")
            if question.lower() == "quit":
                print("See you next session!")
                break
            answer = ask_about_documents(context, question)
            print(f"\nAI: {answer}\n")
