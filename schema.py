from pydantic import BaseModel


class Book(BaseModel):
    id_: int
    name: str
    isbn: str
    type_: str
    publish: str
    price: float


if __name__ == "__main__":

    book = {
        "id_": 1,
        "name": "The Lost Chronicles",
        "isbn": "978-1234567890",
        "type_": "Fiction",
        "publish": "2023-01-15",
        "price": 60
    }
    b = Book(**book)
    print(b)
    print(b.id_)