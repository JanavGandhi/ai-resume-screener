from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load once (important for performance)
model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_semantic_similarity(resume_text: str, jd_text: str) -> float:
    embeddings = model.encode(
        [resume_text, jd_text],
        convert_to_tensor=False,
        normalize_embeddings=True
    )

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )

    return float(similarity[0][0])
