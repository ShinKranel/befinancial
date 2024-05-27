from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.db import get_async_session
from src.user.models import User
from src.user.schemas import AddUser

router = APIRouter()


@router.get("/")
async def read_users(session: AsyncSession = Depends(get_async_session)):
    query = select(User).options(joinedload(User.budgets))
    result = await session.execute(query)
    res = result.unique().scalars().all()
    return {"lala": res}


@router.get("/{user_id}")
async def read_user_budgets(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(User).where(User.id == user_id).options(joinedload(User.budgets))
    result = await session.execute(query)
    res = result.unique().scalars().all()
    return {"lala": res[0].budgets}


@router.post("/")
async def add_user(user: AddUser, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(User).values(**user.dict())
    await session.execute(stmt)
    await session.commit()
    return {"stmt": "success"}

