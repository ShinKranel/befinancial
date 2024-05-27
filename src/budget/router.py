from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.budget.models import Budget
from src.budget.schemas import AddBudget
from src.db import get_async_session

router = APIRouter()


@router.get("/")
async def read_budget(session: AsyncSession = Depends(get_async_session)):
    query = select(Budget)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/{budget_id}")
async def read_budget_by_id(budget_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Budget).where(Budget.id == budget_id)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/")
async def add_budget(budget: AddBudget, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Budget).values(**budget.dict())
    await session.execute(stmt)
    await session.commit()
    return {"stmt": "success"}

