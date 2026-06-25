
import streamlit as st
import anthropic
from dotenv import load_dotenv
import os
import PyPDF2
import io

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

system_prompt = """You are a helpful document assistant.
Answer questions based only on the provided documents.
When answering, mention which document the information came from.
If the answer isn't in any document, say so."""

st.title("📄 Kollie's AI Document Assistant")
st.write("Upload text or PDF files and ask questions about them!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "messages" not in st.session_state:
    st.session_state.messages = []

uploaded_files = st.file_uploader(
    "Choose files",
    type=["txt", "pdf"],
    accept_multiple_files=True
)

documents = {}

if uploaded_files:
    for file in uploaded_files:
        try:
            if file.name.endswith(".pdf"):
                pdf_reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
                content = ""
                for page in pdf_reader.pages:
                    content += page.extract_text()
            else:
                content = file.read().decode("utf-8")

            if content.strip() == "":
                st.warning(f"⚠️ {file.name} is empty and was skipped.")
            else:
                documents[file.name] = content
        except Exception as e:
            st.error(f"Could not read {file.name}: {e}")

    if documents:
        st.success(f"✓ Loaded {len(documents)} document(s): {', '.join(documents.keys())}")

        with st.sidebar:
            st.header("📊 Document Stats")
            for name, text in documents.items():
                word_count = len(text.split())
                char_count = len(text)
                st.subheader(name)
                st.write(f"Words: {word_count}")
                st.write(f"Characters: {char_count}")
                st.divider()

            if st.button("🗑️ Clear History"):
                st.session_state.chat_history = []
                st.session_state.messages = []
                st.success("History cleared!")

context = ""
for name, text in documents.items():
    context += f"--- Document: {name} ---\n{text}\n\n"

question = st.text_input("Ask a question about your documents:")

if st.button("Ask"):
    if not documents:
        st.error("Please upload at least one document first.")
    elif not question.strip():
        st.error("Please type a question.")
    else:
        st.session_state.messages.append({
            "role": "user",
            "content": f"Documents:\n{context}\n\nQuestion: {question}"
        })

        try:
            with st.spinner("Thinking..."):
                message = client.messages.create(
                    model="claude-opus-4-6",
                    max_tokens=1024,
                    system=system_prompt,
                    messages=st.session_state.messages
                )
                answer = message.content[0].text

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })
            st.session_state.chat_history.append((question, answer))

        except Exception as e:
            st.error(f"Something went wrong: {e}")

if st.session_state.chat_history:
    st.write("### Conversation History")
    for q, a in reversed(st.session_state.chat_history):
        st.write(f"**You:** {q}")
        st.write(f"**AI:** {a}")
        st.divider()
