import json
from schema import Book

def load_book() -> list:
    with open("book.json") as f:
        books = json.load(f)
        return [Book(**book) for book in books]
