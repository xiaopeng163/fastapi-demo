from fastapi import FastAPI
from fastapi import HTTPException
import uvicorn

from db import load_book

app = FastAPI()


books = load_book()


@app.get("/api/books")
def get_books(type_: str | None = None, id_: int | None = None) -> list:
    result = books
    if type_:
        result = [book for book in books if book.type_ == type_]
    if id_:
        return [book for book in result if book.id_ == id_]
    return result


@app.get("/api/books/{id_}")
def get_book_by_id(id_: int) -> dict:
    result = [book for book in books if book.id_ == id_]
    if result:
        return result[0]
    raise HTTPException(status_code=404, detail=f"No book with _id={id_}")


if __name__ == "__main__":
    uvicorn.run("book:app", reload=True)
