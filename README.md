# WritingStuff

An AI-powered writing assistant and PDF research summarizer micro-SaaS built with FastAPI (backend) and React (frontend).

## Project Overview

WritingStuff is a comprehensive web-based platform that allows users to:

1. Write and compose documents in a rich text editor
2. Upload and view PDFs side by side for research
3. Use AI for writing improvements, document summarization, and semantic search
4. (Future) Add citations, paper recommendations, and collaborative editing

## Tech Stack

### Backend
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **Vector Database**: Pinecone
- **AI Provider**: OpenAI
- **File Storage**: AWS S3 (planned)
- **Authentication**: JWT-based

### Frontend
- **Framework**: React with Vite
- **UI**: Tailwind CSS + shadcn components
- **PDF Viewer**: react-pdf (planned)
- **State Management**: React Context API / Hooks

## Project Structure

```
writingstuff/
├── backend/             # FastAPI backend
│   ├── core/            # Core configurations and settings
│   ├── models/          # Database models and schemas
│   ├── routers/         # API route definitions
│   ├── services/        # Business logic services
│   ├── utils/           # Utility functions
│   ├── main.py          # Application entry point
│   ├── requirements.txt # Python dependencies
│   └── Dockerfile       # Backend container definition
│
├── frontend/            # React frontend
│   ├── src/
│   │   ├── components/  # Reusable UI components
│   │   ├── pages/       # Page components
│   │   ├── utils/       # Utility functions
│   │   ├── services/    # API service integrations
│   │   ├── App.jsx      # Main application component
│   │   └── main.jsx     # Application entry point
│   ├── package.json     # JavaScript dependencies
│   └── Dockerfile       # Frontend container definition
│
└── docker-compose.yml   # Multi-container definition
```

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Node.js (for local frontend development)
- Python 3.10+ (for local backend development)

### Environment Variables

1. Copy the example environment file:
   ```
   cp backend/.env.example backend/.env
   ```

2. Fill in your API keys and credentials:
   - OpenAI API key
   - Pinecone API key
   - AWS credentials (if using S3)

### Running the Application

To start the entire application stack with Docker Compose:

```bash
docker-compose up
```

This will start:
- Backend API at http://localhost:8000
- Frontend application at http://localhost:3000
- PostgreSQL database

### API Documentation

Once the backend is running, you can access the automatically generated API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Current Implementation Status

- [x] Project structure and Docker setup
- [x] Basic frontend pages (Login, Register, Dashboard, Editor, PDF Viewer)
- [x] Basic backend API structure (auth, documents, AI routes)
- [ ] Rich text editor integration
- [ ] PDF chunking and indexing
- [ ] Pinecone vector storage integration
- [ ] AI summarization and writing improvements
- [ ] User authentication with JWT

## License

This project is built for demonstration purposes and is not licensed for commercial use.
