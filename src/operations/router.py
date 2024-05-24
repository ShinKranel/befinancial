from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session
from src.operations.models import Operation
from src.operations.schemas import AddOperation

router = APIRouter()


@router.get("/operations")
async def read_operations(session: AsyncSession = Depends(get_async_session)):
    query = select(Operation)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/operations/{operation_id}")
async def read_operation_by_id(operation_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Operation).where(Operation.id == operation_id)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/operations")
async def add_operation(operation: AddOperation, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Operation).values(**operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"stmt": "success"}

