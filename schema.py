from pydantic import BaseModel


class BookInput(BaseModel):
    name: str
    isbn: str
    type_: str
    publish: str
    price: float

    class Config:
        json_schema_extra = {
            "example": {
                "name": "The Book Name",
                "isbn": "abcd-1234",
                "type_": "Fiction",
                "publish": "2023-10-20",
                "price": 120,
            }
        }


class BookOutput(BookInput):
    id_: int

    class Config:
        json_schema_extra = {
            "example": {
                "id_": 1,
                "name": "The Book Name",
                "isbn": "abcd-1234",
                "type_": "Fiction",
                "publish": "2023-10-20",
                "price": 120,
            }
        }


if __name__ == "__main__":
    book = BookOutput(
        id_=10, name="test", isbn="1234", type_="test", publish="2023", price="30"
    )
    print(book)
    print(book.model_dump())
    print(book.model_dump_json())
    print(book.isbn)
    print(book.id_)
