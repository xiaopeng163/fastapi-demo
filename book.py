from fastapi import FastAPI
from fastapi import HTTPException
import uvicorn

from db import load_book

app = FastAPI()


books = load_book()


@app.get("/api/books")
def get_books(_type: str | None = None, _id: int | None = None) -> list:
    result = books
    if _type:
        result = [book for book in books if book["_type"] == _type]
    if _id:
        return [book for book in result if book["_id"] == _id]
    return result


@app.get("/api/books/{_id}")
def get_book_by_id(_id: int) -> dict:
    result = [book for book in books if book["_id"] == _id]
    if result:
        return result[0]
    raise HTTPException(status_code=404, detail=f"No book with _id={_id}")


if __name__ == "__main__":
    uvicorn.run("book:app", reload=True)
