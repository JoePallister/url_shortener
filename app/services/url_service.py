import random
import string
from sqlalchemy.orm import Session
from repositories.url_repository import write_url_to_db, fetch_all_urls, fetch_long_url

BASE62 = string.digits + string.ascii_letters  # 0-9a-zA-Z


def make_short_url(db: Session, url: str) -> str:
    if not validate_url(url):
        raise ValueError("Invalid URL")

    short_url = generate_short_url(db, length=8)
    write_url_to_db(db, short_url=short_url, long_url=url)
    return short_url


def generate_short_url(db: Session, length: int = 8) -> str:
    candidate = "".join(random.choices(BASE62, k=length))
    while fetch_long_url(db, candidate):
        candidate = "".join(random.choices(BASE62, k=length))
    return candidate


def get_all_urls(db: Session):
    return fetch_all_urls(db)


def expand_short_url(short_url: str) -> str:
    return short_url


def validate_url(url: str) -> bool:
    return True
