from fastapi import HTTPException
from fastapi import Depends
from fastapi import APIRouter
from sqlmodel import Session, select

from db import get_session
from schema import BookInput, Book

router = APIRouter(prefix="/api/books")


@router.get("/")
def get_books(
    type_: str | None = None,
    id_: int | None = None,
    session: Session = Depends(get_session),
) -> list[Book]:
    query = select(Book)
    if type_:
        query = query.where(Book.type_ == type_)
    if id_:
        query = query.where(Book.id_ == id_)
    return session.exec(query).all()


@router.get("/{id_}")
def get_book_by_id(id_: int, session: Session = Depends(get_session)) -> Book:
    book = session.get(Book, id_)
    if book:
        return book
    else:
        raise HTTPException(status_code=404, detail=f"No book with _id={id_}")


@router.post("/")
def add_book(book: BookInput, session: Session = Depends(get_session)) -> Book:
    new_book = Book.from_orm(book)
    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    return new_book


@router.delete("/{id_}")
def delete_book(id_: int, session: Session = Depends(get_session)):
    book = session.get(Book, id_)
    if book:
        session.delete(book)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"No book with _id={id_}")


@router.put("/api/books/{id_}")
def update_book(
    id_: int, new_book: BookInput, session: Session = Depends(get_session)
) -> Book:
    book = session.get(Book, id_)
    if book:
        book.name = new_book.name
        book.isbn = new_book.isbn
        book.type_ = new_book.type_
        book.publish = new_book.publish
        book.price = new_book.price
        session.commit()
        return book
    else:
        raise HTTPException(status_code=404, detail=f"No book with _id={id_}")
