import json
from schema import BookOutput


def load_book() -> list:
    with open("book.json") as f:
        books = json.load(f)
        return [BookOutput(**book) for book in books]


def save_book(books: list[BookOutput]):
    with open("book.json", "w") as f:
        json.dump([book.model_dump() for book in books], f, indent=4)
