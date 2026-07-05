from sqlalchemy.orm import Session
from app.models.url import URL
from redis import Redis


def write_url_to_db(db: Session, short_url: str, long_url: str):
    url = URL(short_url=short_url, long_url=long_url)
    db.add(url)
    db.commit()
    db.refresh(url)
    return url


def fetch_all_urls(db: Session):
    return db.query(URL).all()


def fetch_long_url(redis: Redis, db: Session, short_url: str):
    long_url = redis.get(short_url)

    if long_url is not None:
        return long_url
    url = db.query(URL).filter(URL.short_url == short_url).first()
    if url:
        redis.set(short_url, url.long_url)
        return url.long_url
    return None


def does_short_url_exist(db: Session, short_url: str):
    url = db.query(URL).filter(URL.short_url == short_url).first()
    if url:
        return True
    return False
