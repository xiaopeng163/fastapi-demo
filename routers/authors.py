from fastapi import HTTPException
from fastapi import Depends
from fastapi import APIRouter
from sqlmodel import Session, select

from db import get_session
from schema import AuthorInput, Author, BookInput, Book, AuthorOutput


router = APIRouter(prefix="/api/authors")


@router.post("/")
def add_author(author: AuthorInput, session: Session = Depends(get_session)) -> Author:
    new_author = Author.from_orm(author)
    session.add(new_author)
    session.commit()
    session.refresh(new_author)
    return new_author


@router.get("/")
def get_authors(
    session: Session = Depends(get_session),
) -> list[Author]:
    query = select(Author)
    return session.exec(query).all()


@router.get("/{id_}")
def get_author_by_id(id_: int, session: Session = Depends(get_session)) -> AuthorOutput:
    author = session.get(Author, id_)
    if author:
        return author
    else:
        raise HTTPException(status_code=404, detail=f"No author with _id={id_}")


@router.post("/{id_}/books")
def add_book_by_author_id(
    id_: int, book: BookInput, session: Session = Depends(get_session)
) -> Book:
    author = session.get(Author, id_)
    if author:
        new_book = Book.from_orm(book, update={"auth_id": author.id_})
        session.add(new_book)
        session.commit()
        session.refresh(new_book)
        return new_book
    else:
        raise HTTPException(status_code=404, detail=f"No author with _id={id_}")
