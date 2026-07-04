from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from typing_extensions import Annotated

from app.database import Base, engine, get_db
from app.services.url_service import process_long_url, expand_short_url, get_all_urls
from app.schemas.url import ShortenRequest

app = FastAPI()
Base.metadata.create_all(bind=engine)

DBSession = Annotated[Session, Depends(get_db)]


@app.get("/urls")
def all_urls(db: DBSession):
    return get_all_urls(db)


@app.post("/shorten")
def shorten_url(db: DBSession, body: ShortenRequest):
    print(body.url)
    return {"short_url": process_long_url(db, str(body.url))}


@app.get("/")
def expand_url(db: DBSession, short_url: str):
    return expand_short_url(db, short_url)
