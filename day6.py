import anthropic 
from dotenv import load_dotenv
import os 
load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# System promt gives the AI a role
system_prompt ="""you are an expert AI engineering mentor.
Your student is Kollie, a beginner learning to become
an AI engineer in ^ months.
Keep answer clear, simple, and encouraging.
use analogie to explin complex concepts."""

# This list stores the conversation history
conversation_history =[]

def ask_ai(question):
    #add user question to history
    conversation_history.append({
        "role": "user",
        "content": question
    })

    #Send full history to AI every time
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        system=system_prompt,
        messages=conversation_history
    )

    response = message.content[0].text

    # Add AIrespone to history
    conversation_history.append[{
        "role": "assitant",
        "content": response
    }]
    return response

def handle_command(command):
    if command == "help": 
        print("\nComands:")
        print("/help - show commands")
        print("/history - show conversation so far")
        print("clear -start fresh conversation")
        print("quit - exit\n")
    elif command == "/history":
        print("\n--- conversation ---")
        for msg in conversation_history:
            role ="you" if msg["role"] == "user" else "AI"
            print(f"{role}: {msg['content'][:100]}...")
        print("----------------------------\n")
    elif command == "/clear":
        conversation_history.clear()
        print("\nconversation cleared! starting fresh.\n")

print("AI Engineering Mentor Ready!")
print("Type /help for commands or quit to exit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("see you next session!")
        break
    elif user_input.startswith("/"):
        handle_command(user_input)
    else:
        response = ask_ai(user_input)
        print(f"\nAI: {response}\n")   