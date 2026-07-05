from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from typing_extensions import Annotated
from redis import Redis

from app.database import Base, engine, get_db, get_redis
from app.services.url_service import process_long_url, expand_short_url, get_all_urls
from app.schemas.url import ShortenRequest

app = FastAPI()
Base.metadata.create_all(bind=engine)

DBSession = Annotated[Session, Depends(get_db)]
RedisClient = Annotated[Redis, Depends(get_redis)]


@app.get("/urls")
def all_urls(db: DBSession):
    return get_all_urls(db)


@app.post("/shorten")
def shorten_url(db: DBSession, body: ShortenRequest):
    return {"short_url": process_long_url(db, str(body.url))}


@app.get("/{short_url}")
def expand_url(redis: RedisClient, db: DBSession, short_url: str):
    long_url = expand_short_url(redis, db, short_url)
    if long_url is None:
        raise HTTPException(status_code=404)
    return RedirectResponse(url=long_url)
