from typing import List, Optional
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from .models import User
from .schemas import UserDeletedResponse, UserResponse, UserCreate, UserUpdate


def get_all(*, db_session: Session) -> List[UserResponse]:
    return db_session.query(User).all()


def get_by_id(*, user_id: int, db_session: Session) -> Optional[UserResponse]:
    user = db_session.query(User).filter_by(user_id=user_id).one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def create(*, user: UserCreate, db_session: Session) -> UserResponse:
    new_user = User(**user.model_dump())
    db_session.add(new_user)
    try:
        db_session.commit()
    except IntegrityError as exc:
        raise HTTPException(status_code=409, details="User already exists")
    db_session.refresh(new_user)
    return dict(new_user)


def update(*, user_id: int, user: UserUpdate, db_session: Session) -> UserResponse:
    db_user = db_session.query(User).filter_by(user_id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.model_dump().items():
        setattr(db_user, key, value)
    db_session.commit()
    db_session.refresh(db_user)
    return UserResponse(**dict(db_user))


def delete(*, user_id: int, db_session: Session) -> UserDeletedResponse:
    db_user = db_session.query(User).filter_by(user_id=user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_session.delete(db_user)
    db_session.commit()
    return UserDeletedResponse(**dict(db_user))
