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


class AuthorInput(SQLModel):
    name: str
    nationality: str


class Author(AuthorInput, table=True):
    id_: int | None = Field(primary_key=True, default=None)
