from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(index=True, nullable=False)
    max_capacity: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)

    def __init__(self, username: str, max_capacity: int, description: Optional[str] = None):
        self.username = username
        self.max_capacity = max_capacity
        self.description = description

    def __iter__(self):
        yield "user_id", self.user_id
        yield "username", self.username
        yield "max_capacity", self.max_capacity
        yield "description", self.description
