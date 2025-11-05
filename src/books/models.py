import uuid
from datetime import datetime
from sqlmodel import SQLModel, Field, Column
from sqlalchemy.dialects import postgresql as pg

class Book(SQLModel, table=True):
    __tablename__ = "books"

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            nullable=False,
            default=uuid.uuid4
        )
    )
    title: str = Field(nullable=False)
    author: str = Field(nullable=False)
    publisher: str = Field(nullable=True)
    published_date: str = Field(nullable=True)
    page_count: str = Field(nullable=True)
    language: str = Field(nullable=True)
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))


    def __str__(self):
        return f"<Book {self.title}>"