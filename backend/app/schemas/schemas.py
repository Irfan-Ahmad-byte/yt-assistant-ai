from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    full_name: str | None = None

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class UserInDB(UserBase):
    id: int

