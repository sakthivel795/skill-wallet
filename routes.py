from fastapi import APIRouter, HTTPException

from backend.models import (
    DocumentRequest,
    DocumentResponse
)

from ai_core.gemini_generator import (
    GeminiDocumentGenerator
)

router = APIRouter()


@router.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "LegalEase API"
    }


@router.post(
    "/generate",
    response_model=DocumentResponse
)
async def generate_document(
    request: DocumentRequest
):

    try:

        generator = GeminiDocumentGenerator()

        generated_document = generator.generate_document(
            document_type=request.document_type,
            parties=request.parties,
            terms=request.terms,
            dates=request.dates
        )

        return DocumentResponse(
            success=True,
            document=generated_document,
            document_type=request.document_type
        )

    except ValueError as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Document generation failed: {str(error)}"
        )