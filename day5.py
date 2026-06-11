import anthropic

client = anthropic.Anthropic(api_key="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")

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