from sqlmodel import SQLModel, Field


class BookInput(SQLModel):
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


class Book(BookInput, table=True):
    id_: int | None = Field(primary_key=True, default=None)


if __name__ == "__main__":
    book = BookOutput(
        id_=10, name="test", isbn="1234", type_="test", publish="2023", price="30"
    )
    print(book)
    print(book.model_dump())
    print(book.model_dump_json())
    print(book.isbn)
    print(book.id_)
