import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


# Enums --------------------------------


# Tables -------------------------------
class Base(DeclarativeBase):
    pass


class Budget(Base):
    __tablename__ = "budget"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    value: Mapped[int]

