import pandas as pd
import numpy as np
import time

from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer("all-mpnet-base-v2")
faq_embeddings = encoder.encode(faq_df["question"].tolist())

print(f"Sample (first 10 dimensions): {faq_embeddings[0][:10]}")

def cosine_dist(a: np.array, b: np.array):
    """Compute cosine distance between two sets of vectors."""
    a_norm = np.linalg.norm(a, axis=1)
    b_norm = np.linalg.norm(b) if b.ndim == 1 else np.linalg.norm(b, axis=1)
    sim = np.dot(a, b) / (a_norm * b_norm)
    return 1 - sim


def semantic_search(query: str) -> tuple:
    """Find the most similar FAQ question to the query."""
    query_embedding = encoder.encode([query])[0]

    distances = cosine_dist(faq_embeddings, query_embedding)

    # Find the most similar question (lowest distance)
    best_idx = int(np.argmin(distances))
    best_distance = distances[best_idx]

    return best_idx, best_distance