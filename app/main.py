from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from typing_extensions import Annotated

from database import Base, engine, get_db

app = FastAPI()
Base.metadata.create_all(bind=engine)

DBSession = Annotated[Session, Depends(get_db)]


@app.get("/")
def root():
    return {"message": "Hello World!"}


@app.post("/shorten")
def shorten_url(db: DBSession, url: str):
    pass


@app.get("/expand")
def expand_url(db: DBSession, short_url: str):
    pass
