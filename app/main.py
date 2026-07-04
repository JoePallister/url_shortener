from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from typing_extensions import Annotated

from database import Base, engine, get_db
from services.url_service import process_long_url, expand_short_url, get_all_urls
from schemas.url import ShortenRequest

app = FastAPI()
Base.metadata.create_all(bind=engine)

DBSession = Annotated[Session, Depends(get_db)]


@app.get("/")
def root():
    return {"message": "Hello World!"}


@app.get("/urls")
def all_urls(db: DBSession):
    return get_all_urls(db)


@app.post("/shorten")
def shorten_url(db: DBSession, body: ShortenRequest):
    return process_long_url(db, str(body.url))


@app.get("/expand")
def expand_url(db: DBSession, short_url: str):
    return expand_short_url(db, short_url)
