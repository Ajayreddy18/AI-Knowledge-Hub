from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


# Load local embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Store text chunks
documents = []

# FAISS index
dimension = 384
index = faiss.IndexFlatL2(dimension)

def split_text(text, chunk_size=200):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)

    return chunks

def chunk_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks


def add_to_index(text):
    
    chunks = split_text(text)   # 👈 important

    embeddings = model.encode(chunks)

    index.add(embeddings)

    documents.extend(chunks)
    
def search(query):
    try:
        print("---- DEBUG START ----")

        query_vector = embeddings(query)   # IMPORTANT
        D, I = index.search(query_vector, k=5)  # YOU WERE MISSING THIS

        print("Documents length:", len(documents))
        print("Raw Index Output (I):", I)

        results = []

        for i in I[0]:
            print("Checking index:", i)

            if 0 <= i < len(documents):
                results.append(documents[i])
            else:
                print("Invalid index skipped:", i)

        print("Final Results:", results)
        print("---- DEBUG END ----")

        return results if results else ["No results found"]

    except Exception as e:
        print("Search Error:", str(e))
        return ["Error in search"]