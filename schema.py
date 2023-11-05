from sqlmodel import SQLModel, Field, Relationship


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
    auth_id: int = Field(foreign_key="author.id_")
    author: "Author" = Relationship(back_populates="books")


class AuthorInput(SQLModel):
    name: str
    nationality: str


class AuthorOutput(AuthorInput):
    id_: int
    books: list[Book] = []


class Author(AuthorInput, table=True):
    id_: int | None = Field(primary_key=True, default=None)
    books: list[Book] = Relationship(back_populates="author")
