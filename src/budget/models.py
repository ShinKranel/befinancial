import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

from src.user.models import User


# Enums --------------------------------


# Tables -------------------------------
class Base(DeclarativeBase):
    pass


class Budget(Base):
    __tablename__ = "budget"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    user: Mapped[User] = relationship(back_populates="children")
    value: Mapped[float]

