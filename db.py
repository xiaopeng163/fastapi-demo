import json


def load_book() -> list:
    with open("book.json") as f:
        books = json.load(f)
        return books
