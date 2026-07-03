from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import Base, engine, get_db

app = FastAPI()
Base.metadata.create_all(bind=engine)
