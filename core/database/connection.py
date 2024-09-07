from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
import os
from typing import Annotated
from fastapi import Depends
from core.utils.utils import config_data


Base = declarative_base()


match config_data["db"]["type"]:
    case "sqlite":
        
        absolute_directory = os.path.dirname(os.path.abspath(__file__))
        file_directory = "file"
        db_directory = os.path.join(absolute_directory, file_directory)
        db_file_name = "database.db"
    
        if not os.path.exists(db_directory):
            os.makedirs(db_directory)
            
        file_path = os.path.join(db_directory, db_file_name)
        with open(file_path, 'w') as db_file:
            pass
        
        db_uri = f'sqlite+aiosqlite:///{file_path}'
        engine = create_async_engine(db_uri)
    
    # case "postgres":
    #     db_uri = f'postgresql+asyncpg://{configs.db_username}:{configs.db_password}@{configs.db_host}:{configs.db_port}/{configs.db_name}'
    #     engine = create_async_engine(db_uri, pool_size=configs.db_pool_size, max_overflow=configs.db_max_overflow)
    
    # case "mysql":
    #     db_uri = f'mysql+aiomysql://{configs.db_username}:{configs.db_password}@{configs.db_host}:{configs.db_port}/{configs.db_name}'
    #     engine = create_async_engine(db_uri, pool_size=configs.db_pool_size, max_overflow=configs.db_max_overflow)

    case _:
        raise ValueError("Database connection failed")


async_session = async_sessionmaker(engine, expire_on_commit=False)


async def init_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def async_connection():
    async with async_session() as session:
        yield session


db_session = Annotated[AsyncSession, Depends(async_connection)]