from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Server is starting...")

    # ✅ Initialize the database
    await init_db()
    print("✅ Database initialized successfully.")

    # Yield control to the running app
    yield

    # Clean shutdown (optional: close connections, cleanup)
    print("🛑 Server has been stopped.")


version = "v1"

app = FastAPI(
    title = "Book Store",
    description="A Restapi for Book Review Service",
    version=version,
    lifespan=lifespan
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])

