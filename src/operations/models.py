import enum

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from src.config import settings


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
    amount: Mapped[int] = mapped_column(nullable=False)
    type: Mapped[OperationType] = mapped_column(nullable=False)

print(settings.DB_NAME)
