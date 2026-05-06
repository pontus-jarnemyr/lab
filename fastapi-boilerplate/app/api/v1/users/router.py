from typing import List, Optional
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from .service import get_all, get_by_id, create, update, delete
from .schemas import UserResponse, UserCreate, UserUpdate, UserDeletedResponse


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserResponse])
def get_all_users(db_session: Session = Depends(get_db)) -> List[UserResponse]:
    return get_all(db_session=db_session)


@router.get("/{user_id}", response_model=Optional[UserResponse])
def get_user_by_id(user_id: str, db_session: Session = Depends(get_db)) -> Optional[UserResponse]:
    return get_by_id(user_id=user_id, db_session=db_session)


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db_session: Session = Depends(get_db)) -> UserResponse:
    return create(user=user, db_session=db_session)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db_session: Session = Depends(get_db)) -> UserResponse:
    return update(user_id=user_id, user=user, db_session=db_session)


@router.delete("/{user_id}", response_model=UserDeletedResponse)
def delete_user(user_id: int, db_session: Session = Depends(get_db)) -> UserDeletedResponse:
    return delete(user_id=user_id, db_session=db_session)
