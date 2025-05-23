# Resume Analyzer API (No SpaCy, No PostgreSQL)

A FastAPI-based project to upload and analyze resumes using basic text processing.  
Built with simplicity, performance, and GitHub-readiness in mind.

## Features

- Upload resume files (`.pdf`, `.docx`, `.txt`)
- Extract plain text content
- Basic keyword and content analysis
- Built using **FastAPI**
- No external NLP libraries like `spaCy`
- No database dependencies (data held in memory or temp storage)

## Endpoints

- `POST /upload/` – Upload a resume and extract content
- `GET /health/` – Check API health

## Technologies Used

- Python 3.11
- FastAPI
- Uvicorn
- Python-Multipart (for file uploads)

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/rezakeyhani/resume-analyzer-api.git
#   r e s u m e - a n a l y z e r - a p i  
 