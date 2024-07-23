from typing import Optional
from uuid import UUID
from fastapi import APIRouter, File, Form, UploadFile

from services.document_service import DocumentServiceImpl
from schemas.document import DocumentWriteManualSchema, DocumentWriteSchema

document_service = DocumentServiceImpl()
router = APIRouter()


@router.post("/document")
def create_document(
    name: Optional[str] = Form(...),
    file: UploadFile = File(...),
):
    document = DocumentWriteSchema(name=name)
    return document_service.create_document(document, file)

@router.post("/document/manual")
def create_document_manual(
    document: DocumentWriteManualSchema,
):
    return document_service.create_document_manual(document)

@router.get("/document/{document_id}")
def get_document(document_id: UUID):
    return document_service.get_document(document_id)


@router.delete("/document/{document_id}")
def delete_document(document_id: UUID):
    return document_service.delete_document(document_id)


@router.get("/documents")
def get_all_document():
    return document_service.get_all_document()


@router.get("/document/{document_id}/content")
def get_document_content(document_id: UUID):
    return document_service.get_document_content(document_id)
