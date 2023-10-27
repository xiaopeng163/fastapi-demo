from fastapi import FastAPI
from fastapi import HTTPException
import uvicorn
from sqlmodel import create_engine, SQLModel, Session, select

from db import load_book, save_book
from schema import BookInput, BookOutput, Book

app = FastAPI(title="Book API")


books = load_book()

engine = create_engine(
    "sqlite:///book.db", connect_args={"check_same_thread": False}, echo=True
)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.get("/api/books")
def get_books(type_: str | None = None, id_: int | None = None) -> list[Book]:
    with Session(engine) as session:
        query = select(Book)
        if type_:
            query = query.where(Book.type_ == type_)
        if id_:
            query = query.where(Book.id_ == id_)
        return session.exec(query).all()


@app.get("/api/books/{id_}")
def get_book_by_id(id_: int) -> Book:
    with Session(engine) as session:
        book = session.get(Book, id_)
        if book:
            return book
        else:
            raise HTTPException(status_code=404, detail=f"No book with _id={id_}")


@app.post("/api/books")
def add_book(book: BookInput) -> Book:
    with Session(engine) as session:
        new_book = Book.from_orm(book)
        session.add(new_book)
        session.commit()
        session.refresh(new_book)
        return new_book


@app.delete("/api/books/{id_}")
def delete_book(id_: int):
    matches = [book for book in books if book.id_ == id_]
    if matches:
        books.remove(matches[0])
        save_book(books)
    else:
        raise HTTPException(status_code=404, detail=f"No book with _id={id_}")


@app.put("/api/books/{id_}")
def update_book(id_: int, new_book: BookInput) -> BookOutput:
    matches = [book for book in books if book.id_ == id_]
    if matches:
        book = matches[0]
        book.name = new_book.name
        book.isbn = new_book.isbn
        book.type_ = new_book.type_
        book.publish = new_book.publish
        book.price = new_book.price
        save_book(books)
        return book
    else:
        raise HTTPException(status_code=404, detail=f"No book with _id={id_}")


if __name__ == "__main__":
    uvicorn.run("book:app", reload=True)
