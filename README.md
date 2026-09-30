# LegalEase

LegalEase is an AI-assisted legal document drafting application.

## Features

- AI-powered legal document drafting
- Google Gemini integration
- FastAPI backend
- Streamlit frontend
- Editable document preview
- TXT export
- DOCX export
- PDF export
- Logo branding
- Terms table
- PDF footer
- API health check
- Input validation

## Architecture

Streamlit
    |
    v
FastAPI
    |
    v
Gemini
    |
    v
Generated document
    |
    +---- TXT
    |
    +---- DOCX
    |
    +---- PDF

## Installation

Create a virtual environment:

```bash
python -m venv venv