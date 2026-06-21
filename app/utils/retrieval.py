from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.chunk import Chunk
from app.utils.embedding import generate_embedding


def retrieve_chunks(
    question: str,
    db: Session,
    top_k: int = 5
):
    question_embedding = generate_embedding(
        question
    )

    chunks = db.execute(
        select(Chunk)
        .order_by(
            Chunk.embedding.cosine_distance(
                question_embedding
            )
        )
        .limit(top_k)
    ).scalars().all()

    return [
        chunk.content
        for chunk in chunks
    ]