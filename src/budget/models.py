from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db import Base


# Enums --------------------------------


# Tables -------------------------------
class Budget(Base):
    __tablename__ = "budget"

    id: Mapped[int] = mapped_column(primary_key=True)

    value: Mapped[float]

    # foreign keys
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))

    # relationships
    user = relationship("User", back_populates="budgets")
    operations = relationship("Operation", back_populates="budget")
