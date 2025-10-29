import os
from dotenv import load_dotenv
from sqlalchemy import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DB_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:example@localhost:5432/mi_db")

engine = create_async_engine(DB_URL, echo=True, future=True)

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# This gives the endpoint that is requiring a session with the db and its kept as context, 
# it can be used and then it is closed because of the yield
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session 
    # yield -> maneja el contexto (ciclo de vida) de la sesion
