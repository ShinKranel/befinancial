import enum
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


# Enums --------------------------------
class OperationType(enum.Enum):
    income = "income"
    outcome = "outcome"


# Tables -------------------------------
class Base(DeclarativeBase):
    pass


class Operation(Base):
    __tablename__ = "operation"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    budget_id: Mapped[int] = mapped_column(ForeignKey("Budget.id"))
    amount: Mapped[int]
    type: Mapped[OperationType]
    datetime: Mapped[datetime]
