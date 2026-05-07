import streamlit as st

from pdf_processor import extract_text_from_pdf
from chunking import chunk_documents
from embeddings import create_embeddings
from vector_store import VectorStore
from retriever import retrieve
from prompts import build_prompt
from llm import generate_response

st.title("PDF Question Answering Assistant")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:

    file_path = f"data/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded")

    documents = extract_text_from_pdf(file_path)

    chunks = chunk_documents(documents)

    embeddings = create_embeddings(chunks)

    dimension = len(embeddings[0])

    vector_store = VectorStore(dimension)

    vector_store.add_embeddings(embeddings, chunks)

    question = st.text_input("Ask a question")

    if question:

        retrieved_chunks = retrieve(question, vector_store)

        context = "\n".join([c["text"] for c in retrieved_chunks])

        prompt = build_prompt(context, question)

        answer = generate_response(prompt)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Sources")
        unique_pages = sorted(set(c["page"] for c in retrieved_chunks))
        for page in unique_pages:
            st.write(f"Page {page}")        