


from typing import Optional
from fastapi import APIRouter, File, Form, UploadFile

from services.document_service import DocumentServiceImpl
from schemas.document import DocumentWriteSchema

document_service = DocumentServiceImpl()
router = APIRouter()

@router.post("/document")
def create_document(
    name: Optional[str] = Form(...),
    file: UploadFile = File(...),
):
    document = DocumentWriteSchema(name=name)
    return document_service.create_document(document, file)

@router.get("/document/{document_id}")
def get_document(document_id: int):
    return document_service.get_document(document_id)


@router.delete("/document/{document_id}")
def delete_document(document_id: int):
    return document_service.delete_document(document_id)