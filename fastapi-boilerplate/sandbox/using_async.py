"""
We should probably use SQLModel instead. It has built-in async support and
integrates very well with the rest of the she-bang.
"""

from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlmodel import SQLModel, create_engine, Session, Field, select
from sqlalchemy.ext.asyncio import AsyncSession
import pytest
from httpx import AsyncClient

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
async_session = AsyncSession(engine)

async def get_db():
    async with async_session() as session:
        yield session

# Models
class User(SQLModel, table=True):
    user_id: int = Field(default=None, primary_key=True)
    username: str
    max_capacity: int

class UserDeletedResponse(SQLModel):
    user_id: int
    username: str

# Service
async def delete(*, user_id: int, db_session: AsyncSession) -> UserDeletedResponse:
    statement = select(User).filter_by(user_id=user_id)
    result = await db_session.execute(statement)
    db_user = result.scalars().first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    await db_session.delete(db_user)
    await db_session.commit()
    return UserDeletedResponse(**dict(db_user))

# Router
router = APIRouter()

@router.delete("/{user_id}", response_model=UserDeletedResponse)
async def delete_user(user_id: int, db_session: AsyncSession = Depends(get_db)) -> UserDeletedResponse:
    return await delete(user_id=user_id, db_session=db_session)

# FastAPI app
app = FastAPI()
app.include_router(router, prefix="/api/v1/users")

# Tests
@pytest.mark.asyncio
async def test_delete_user(async_client: AsyncClient):
    resp = await async_client.post("/api/v1/users", json={"max_capacity": 1, "username": "hehe"})
    assert resp.status_code == 201
    new_user = resp.json()
    resp = await async_client.delete(f"/api/v1/users/{new_user['user_id']}")
    assert resp.status_code == 200
