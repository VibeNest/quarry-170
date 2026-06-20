import json
import numpy as np

from app.models.chunk import Chunk
from app.utils.embedding import generate_embedding


def cosine_similarity(
    a,
    b
):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a)
        * np.linalg.norm(b)
    )


def retrieve_chunks(
    question: str,
    chunks
):
    question_embedding = generate_embedding(
        question
    )

    scores = []

    for chunk in chunks:

        chunk_embedding = json.loads(
            chunk.embedding
        )

        score = cosine_similarity(
            question_embedding,
            chunk_embedding
        )

        scores.append(
            (
                score,
                chunk
            )
        )

    scores.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return [
        chunk.content
        for score, chunk in scores[:5]
    ]