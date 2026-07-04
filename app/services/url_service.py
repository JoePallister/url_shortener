import random
import string
from sqlalchemy.orm import Session
from app.repositories.url_repository import (
    write_url_to_db,
    fetch_all_urls,
    fetch_long_url,
    does_short_url_exist,
)

BASE62 = string.digits + string.ascii_letters  # 0-9a-zA-Z


def process_long_url(db: Session, url: str) -> str:
    if not validate_url(url):
        raise ValueError("Invalid URL")

    short_url = generate_short_url(db, length=8)
    write_url_to_db(db, short_url=short_url, long_url=url)
    return short_url


def generate_short_url(db: Session, length: int = 8) -> str:
    candidate = "".join(random.choices(BASE62, k=length))
    while does_short_url_exist(db, candidate):
        candidate = "".join(random.choices(BASE62, k=length))
    return candidate


def get_all_urls(db: Session):
    return fetch_all_urls(db)


def expand_short_url(db: Session, short_url: str):
    return fetch_long_url(db, short_url)


def validate_url(url: str) -> bool:
    return True
