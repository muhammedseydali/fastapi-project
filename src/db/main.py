from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from src.config import Config


# ✅ Create the async engine
engine = create_async_engine(
    Config.DATABASE_URL,
    echo=True,
    future=True
)


# ✅ Initialize database (run at startup)
async def init_db():
    from src.books.models import Book  # Import models before creating tables
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


# ✅ Dependency for FastAPI
async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session() as session:
        yield session
