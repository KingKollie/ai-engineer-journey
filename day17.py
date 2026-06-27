import streamlit as st
import requests
import os

API_URL = os.getenv("BACKEND_url", "http://127.0.0.1:8000")

st.title("📄 Kollie's AI Document Assistant")
st.write("Powered by FastAPI + Claude AI")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Check if API is running
try:
    response = requests.get(f"{API_URL}/health")
    if response.status_code == 200:
        st.sidebar.success("✅ API is online")
    else:
        st.sidebar.error("❌ API is offline")
except:
    st.sidebar.error("❌ Cannot reach API — is FastAPI running?")

uploaded_file = st.file_uploader("Choose a text or PDF file", type=["txt", "pdf"])

document_text = ""

if uploaded_file:
    try:
        if uploaded_file.name.endswith(".pdf"):
            import PyPDF2
            import io
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
            for page in pdf_reader.pages:
                document_text += page.extract_text()
        else:
            document_text = uploaded_file.read().decode("utf-8")
        st.success(f"✓ Loaded {uploaded_file.name}")
    except Exception as e:
        st.error(f"Could not read file: {e}")

question = st.text_input("Ask a question about your document:")

if st.button("Ask"):
    if not document_text:
        st.error("Please upload a document first.")
    elif not question.strip():
        st.error("Please type a question.")
    else:
        try:
            with st.spinner("Thinking..."):
                response = requests.post(
                    f"{API_URL}/ask",
                    json={
                        "question": question,
                        "document": document_text
                    }
                )
                data = response.json()
                answer = data["answer"]
            st.session_state.chat_history.append((question, answer))
        except Exception as e:
            st.error(f"Error talking to API: {e}")

if st.session_state.chat_history:
    st.write("### Conversation History")
    for q, a in reversed(st.session_state.chat_history):
        st.write(f"**You:** {q}")
        st.write(f"**AI:** {a}")
        st.divider()
