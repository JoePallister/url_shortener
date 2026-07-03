import random
import string
from models.url import URL
from sqlalchemy.orm import Session

BASE62 = string.digits + string.ascii_letters  # 0-9a-zA-Z


def make_short_url(db: Session, url: str) -> str:
    if not validate_url(url):
        raise ValueError("Invalid URL")

    short_url = generate_short_url()
    write_url_to_db(db, short_url=short_url, long_url=url)
    return short_url


def write_url_to_db(db: Session, short_url: str, long_url: str):
    url = URL(short_url=short_url, long_url=long_url)
    db.add(url)
    db.commit()
    db.refresh(url)
    return url


def generate_short_url(length: int = 8) -> str:
    return "".join(random.choices(BASE62, k=length))


def expand_short_url(short_url: str) -> str:
    return short_url


def validate_url(url: str) -> bool:
    return True
