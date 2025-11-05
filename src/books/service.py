from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from sqlalchemy.exc import SQLAlchemyError
from .schemas import BookCreateModel, BookUpdateModel
from .models import Book
from datetime import datetime


class BookService:
    async def get_all_books(self, session: AsyncSession):
        try:
            statement = select(Book).order_by(desc(Book.created_at))
            result = await session.exec(statement)
            return result.all()
        except SQLAlchemyError as e:
            print(f"Error fetching books: {e}")
            return []

    async def get_book(self, book_uid: str, session: AsyncSession):
        try:
            statement = select(Book).where(Book.uid == book_uid)
            result = await session.exec(statement)
            book = result.first()
            if not book:
                print(f"⚠️ Book not found for UID: {book_uid}")
            return book
        except SQLAlchemyError as e:
            print(f"Error fetching book: {e}")
            return None

    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        try:
            book_data_dict = book_data.model_dump()
             
            new_book = Book(**book_data_dict) 

            new_book.published_date = datetime.strptime(book_data_dict['published_date'], '%Y-%m-%d') 

            session.add(new_book)

            await session.commit()

            await session.refresh(new_book)

            print(f"Book created successfully: {new_book.title}")

            return new_book
        
        except SQLAlchemyError as e:
            await session.rollback()
            print(f"Error creating book: {e}")
            return None

    async def update_book(self, book_uid: str, book_update: BookUpdateModel, session: AsyncSession):
        try:
            book_to_update = await self.get_book(book_uid, session)
            if not book_to_update:
                print(f"ook not found for UID: {book_uid}")
                return None

            update_data_dict = book_update.model_dump(exclude_unset=True)
            for k, v in update_data_dict.items():
                setattr(book_to_update, k, v)

            session.add(book_to_update)
            await session.commit()
            await session.refresh(book_to_update)
            print(f"✅ Book updated successfully: {book_to_update.title}")
            return book_to_update
        
        except SQLAlchemyError as e:
            await session.rollback()
            print(f"Error updating book: {e}")
            return None

    async def delete_book(self, book_uid: str, session: AsyncSession):
        try:
            book_to_delete = await self.get_book(book_uid, session)
            if not book_to_delete:
                print(f"⚠️ Book not found for UID: {book_uid}")
                return None

            await session.delete(book_to_delete)
            await session.commit()

            print(f"Book deleted successfully: {book_to_delete.title}")
            return {}
        
        except SQLAlchemyError as e:
            await session.rollback()
            print(f"Error deleting book: {e}")
            return None
