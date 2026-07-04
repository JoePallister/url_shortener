from database import Base
from sqlalchemy.orm import Mapped, mapped_column


class URL(Base):
    __tablename__ = "urls"

    short_url: Mapped[str] = mapped_column(primary_key=True)
    long_url: Mapped[str]
