from pydantic import BaseModel, Field


class DocumentRequest(BaseModel):
    document_type: str = Field(
        ...,
        min_length=2,
        max_length=200,
        description="Type of legal document"
    )

    parties: str = Field(
        ...,
        min_length=2,
        max_length=5000,
        description="Parties involved in the agreement"
    )

    terms: str = Field(
        ...,
        min_length=2,
        max_length=10000,
        description="Terms and conditions"
    )

    dates: str = Field(
        ...,
        min_length=2,
        max_length=500,
        description="Effective date or relevant dates"
    )


class DocumentResponse(BaseModel):
    success: bool
    document: str
    document_type: str