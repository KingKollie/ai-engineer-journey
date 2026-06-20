import streamlit as st
import anthropic 
from dotenv import load_dotenv
import os

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("Anthropic_API_KEY"))

system_prompt = """ You are a helpful document assistant.
Answer questions based only on the provided documents.
When answering, mention which document the infromation came from.
If the answer isn't in any document, say so."""

st.title(" Kollie's AI Document Assistant")
st.write("upload text files and ask questions about them!")

uploaded_files = st.file_uploader(
    "choose text file",
    type="txt",
    accept_multiple_files=True
)

if uploaded_files:
    documents = {}
    for file in uploaded_files:
        content = file.read().decode("utf-8")
        documents[file.name] = content
        st.success(f" Loaded {file.name}")

    question = st.text_input("Ask a question about your documents:")

    if question:
        context =""
        for name, text in documents.items():
            context += f"--- Document: {name} ---\n{text}\n\n"
        with st.spinner("Thinking..."):
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
            answer = message.content[0].text

        st.write("### Answer:")
        st.write(answer)
