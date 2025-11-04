from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager

@asynccontextmanager
def life_span(app:FastAPI):
    print('server is starting....')
    yield
    print('server has been stopped')

version = "v1"

app = FastAPI(
    title = "Book Store",
    description="A Restapi for Book Review Service",
    version=version,
    lifespan=life_span
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])