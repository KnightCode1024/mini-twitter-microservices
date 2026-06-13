from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from models import Base


class Message(Base):
    content: Mapped[str] = mapped_column(String(255))
