from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from redis import Redis

from app.config import settings

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


redis = Redis(
    host="localhost",
    port=6379,
    decode_responses=True,
)


def get_redis():
    return redis
