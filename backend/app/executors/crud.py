from sqlalchemy.orm import Session
from app.migrations import users
from app.schemas import schemas


def get_user(db: Session, user_id: int):
    return db.query(users.User).filter(users.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(users.User).filter(users.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = users.User(username=user.username, email=user.email, full_name=user.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(users.User).filter(users.User.id == user_id).first()
    if db_user:
        for key, value in user.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user
