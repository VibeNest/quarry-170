from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
import os


from app.db.dependencies import get_db, get_current_user

from app.models.user import User
from app.models.document import Document
from app.models.chunk import Chunk

from app.utils.pdf import extract_text_from_pdf
from app.utils.chunking import chunk_text
from app.utils.embedding import generate_embedding

router = APIRouter()


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Create uploads folder if not exists
    os.makedirs(
        "uploads",
        exist_ok=True
    )

    # Save uploaded file
    file_path = os.path.join(
        "uploads",
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:
        content = await file.read()
        buffer.write(content)

    # Check empty file
    if os.path.getsize(file_path) == 0:
        os.remove(file_path)

        raise HTTPException(
            status_code=400,
            detail="File is empty"
        )

    # Extract text from PDF
    try:
        text = extract_text_from_pdf(
            file_path
        )

        if not text or not text.strip():

            os.remove(file_path)

            raise HTTPException(
                status_code=400,
                detail=(
                    "Could not extract text from PDF. "
                    "It may be image-based or empty."
                )
            )

    except Exception as e:

        if os.path.exists(file_path):
            os.remove(file_path)

        raise HTTPException(
            status_code=500,
            detail=f"Failed to process PDF: {str(e)}"
        )

    # Create document record
    new_document = Document(
        filename=file.filename,
        owner_id=current_user.id
    )

    db.add(new_document)
    db.commit()
    db.refresh(new_document)

    # Chunk text
    chunks = chunk_text(text)

    # Save chunks + embeddings
    for chunk in chunks:

        embedding = generate_embedding(
            chunk
        )

        db.add(
            Chunk(
                document_id=new_document.id,
                content=chunk,
                embedding = embedding
            )
        )

    # Commit once after loop
    db.commit()

    return {
        "id": new_document.id,
        "filename": new_document.filename,
        "owner_id": new_document.owner_id,
        "chunks_created": len(chunks)
    }