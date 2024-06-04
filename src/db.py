from typing import AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from src.config import settings


engine = create_engine(
    url=settings.DB_URL_psycopg
)

async_engine = create_async_engine(
    url=settings.DB_URL_asyncpg,
)


session_maker = sessionmaker(engine)
async_session_maker = async_sessionmaker(async_engine)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


class Base(DeclarativeBase):
    pass
