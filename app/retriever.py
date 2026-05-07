from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve(question, vector_store):

    query_embedding = model.encode(question)

    results = vector_store.search(query_embedding)

    return results