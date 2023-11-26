from sqlmodel import SQLModel, Field, Column, VARCHAR

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

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


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(sa_column=Column('username', VARCHAR, unique=True, index=True))
    password_hash: str = ''

    def set_password(self, password):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


class UserOutput(SQLModel):
    id: int
    username: str


