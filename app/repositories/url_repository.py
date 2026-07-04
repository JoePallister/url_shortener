from sqlalchemy.orm import Session
from app.models.url import URL


def write_url_to_db(db: Session, short_url: str, long_url: str):
    url = URL(short_url=short_url, long_url=long_url)
    db.add(url)
    db.commit()
    db.refresh(url)
    return url


def fetch_all_urls(db: Session):
    return db.query(URL).all()


def fetch_long_url(db: Session, short_url: str):
    url = db.query(URL).filter(URL.short_url == short_url).first()
    if url:
        return url.long_url
    return None
