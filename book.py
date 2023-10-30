from fastapi import FastAPI
import uvicorn
from sqlmodel import SQLModel

from db import engine
from routers import books
from routers import authors

app = FastAPI(title="Book API")

app.include_router(books.router)
app.include_router(authors.router)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    uvicorn.run("book:app", reload=True)
