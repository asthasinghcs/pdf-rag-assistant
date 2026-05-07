# # PDF Question Answering Assistant

An end-to-end Retrieval-Augmented Generation (RAG) application for querying PDF documents using semantic search and local LLM inference.

## Features

- Upload and process PDF documents

- Extract and chunk document text

- Generate vector embeddings using Sentence Transformers

- Store embeddings using FAISS vector database

- Perform semantic similarity retrieval

- Generate context-aware answers using Llama 3 via Ollama

- Display source page references

## Tech Stack

- Python

- Streamlit

- FAISS

- Sentence Transformers

- Ollama

- Llama 3

- LangChain Text Splitters

## Pipeline

PDF Upload → Text Extraction → Chunking → Embeddings → Vector Search → Context Retrieval → LLM Response

## Run Locally

```bash

pip install -r requirements.txt

streamlit run app/[main.py](http://main.py)

