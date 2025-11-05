# Book Store REST API

A **FastAPI** project to manage books with async database operations using **SQLModel** and **PostgreSQL/SQLite**.  
This project demonstrates modern FastAPI patterns including async DB, Pydantic schemas, routers, and automatic database initialization.

---

## Features

- Full CRUD operations for books
- Async database access using SQLModel and SQLAlchemy
- Pydantic schemas for request validation and response models
- Modular project structure with routers, services, and database layers
- Automatic database table creation on startup
- Versioned API: `/api/v1/books`
- Error handling with `try/except` and `HTTPException`
- FastAPI lifecycle management with `lifespan`

---

## Project Structure

Fastapi_project/
├── main.py # FastAPI entry point
├── venv/ # Virtual environment
├── src/
│ ├── init.py
│ ├── books/
│ │ ├── init.py
│ │ ├── models.py # SQLModel database models
│ │ ├── schemas.py # Pydantic request/response models
│ │ ├── service.py # CRUD logic for books
│ │ └── routes.py # API endpoints
│ └── db/
│ ├── init.py
│ └── main.py # Async DB engine and session
├── requirements.txt # Python dependencies
└── README.md



---

## Requirements

- Python 3.10+
- FastAPI
- SQLModel
- SQLAlchemy
- asyncpg (PostgreSQL) or aiosqlite (SQLite)
- Uvicorn

---

## Installation

1. Clone the repository:
2. 
git clone <repo-url>
cd Fastapi_project
Create and activate virtual environment:

python -m venv venv
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

Install dependencies:

pip install -r requirements.txt

Database Setup

Update your database URL in src/db/main.py or a Config file:

DATABASE_URL = "postgresql+asyncpg://user:password@localhost:5432/bookstore"
# OR for SQLite
# DATABASE_URL = "sqlite+aiosqlite:///./test.db"


Tables are automatically created when the app starts.

# Running the App

# From the project root:

python -m uvicorn main:app --reload


# If your main.py is inside src/:

python -m uvicorn src.main:app --reload


# App runs at http://127.0.0.1:8000

# API docs available at http://127.0.0.1:8000/docs

API Endpoints
Books
Method	Endpoint	Description
GET	/api/v1/books/	Get all books
GET	/api/v1/books/{uid}	Get a single book by UID
POST	/api/v1/books/	Create a new book
PATCH	/api/v1/books/{uid}	Update a book
DELETE	/api/v1/books/{uid}	Delete a book
Example Request

# Create a Book:

POST /api/v1/books/
Content-Type: application/json

{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "publisher": "Prentice Hall",
  "published_date": "2008-08-01",
  "page_count": 464,
  "language": "English"
}

#Contributing

# Fork the repository

# Create your feature branch (git checkout -b feature/my-feature)

# Commit your changes (git commit -m 'Add some feature')

# Push to the branch (git push origin feature/my-feature)

# Open a Pull Request

License

MIT License © 2025
