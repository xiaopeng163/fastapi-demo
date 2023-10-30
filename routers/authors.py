from fastapi import HTTPException
from fastapi import Depends
from fastapi import APIRouter
from sqlmodel import Session, select

from db import get_session
from schema import AuthorInput, Author


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
def get_author_by_id(id_: int, session: Session = Depends(get_session)) -> Author:
    author = session.get(Author, id_)
    if author:
        return author
    else:
        raise HTTPException(status_code=404, detail=f"No author with _id={id_}")
