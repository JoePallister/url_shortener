from sqlalchemy.orm import Session
from models.url import URL


def write_url_to_db(db: Session, short_url: str, long_url: str):
    url = URL(short_url=short_url, long_url=long_url)
    db.add(url)
    db.commit()
    db.refresh(url)
    return url


def fetch_all_urls(db: Session):
    return db.query(URL).all()
