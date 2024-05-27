from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db import Base


# Enums --------------------------------


# Tables -------------------------------
class Budget(Base):
    __tablename__ = "budget"

    id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[float]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))

    user: Mapped["User"] = relationship(back_populates="budgets")
    operations: Mapped[list["Operation"]] = relationship(back_populates="budget")
