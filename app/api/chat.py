from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db.dependencies import get_db, get_current_user
from app.models.user import User
from app.models.chunk import Chunk

from app.schemas.chat import QuestionRequest
from app.utils.retrieval import retrieve_chunks

router = APIRouter()

@router.post("/ask")
def ask_question(
    request: QuestionRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    chunks = db.execute(
        select(Chunk)
    ).scalars().all()

    relevant_chunks = retrieve_chunks(
        request.question,
        chunks
    )

    return {
        "question": request.question,
        "relevant_chunks": relevant_chunks
    }