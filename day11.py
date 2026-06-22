import streamlit as st
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

system_prompt = """You are a helpful document assistant.
Answer questions based only on the provided documents.
When answering, mention which document the information came from.
If the answer isn't in any document, say so."""

st.title("📄 Kollie's AI Document Assistant")
st.write("Upload one or more text files and ask questions about them!")

uploaded_files = st.file_uploader(
    "Choose text files",
    type="txt",
    accept_multiple_files=True
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

documents = {}

if uploaded_files:
    for file in uploaded_files:
        try:
            content = file.read().decode("utf-8")
            if content.strip() == "":
                st.warning(f"⚠️ {file.name} is empty and was skipped.")
            else:
                documents[file.name] = content
        except Exception as e:
            st.error(f"Could not read {file.name}: {e}")

    if documents:
        st.success(f"✓ Loaded {len(documents)} document(s): {', '.join(documents.keys())}")
    else:
        st.warning("No valid documents loaded. Please upload a non-empty .txt file.")

question = st.text_input("Ask a question about your documents:")

if st.button("Ask"):
    if not documents:
        st.error("Please upload at least one document first.")
    elif not question.strip():
        st.error("Please type a question.")
    else:
        context = ""
        for name, text in documents.items():
            context += f"--- Document: {name} ---\n{text}\n\n"

        try:
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
            st.session_state.chat_history.append((question, answer))
        except Exception as e:
            st.error(f"Something went wrong calling the AI: {e}")

if st.session_state.chat_history:
    st.write("### Conversation History")
    for q, a in reversed(st.session_state.chat_history):
        st.write(f"**You:** {q}")
        st.write(f"**AI:** {a}")
        st.divider()