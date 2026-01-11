import nltk
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("punkt", quiet=True)

model = SentenceTransformer("all-MiniLM-L6-v2")

def top_matching_sentences(resume_text: str, jd_text: str, top_k: int = 3):
    sentences = nltk.sent_tokenize(resume_text)

    embeddings = model.encode(
        sentences + [jd_text],
        normalize_embeddings=True
    )

    jd_embedding = embeddings[-1]
    sentence_embeddings = embeddings[:-1]

    scores = cosine_similarity(
        sentence_embeddings,
        [jd_embedding]
    ).flatten()

    ranked = sorted(
        zip(sentences, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:top_k]
