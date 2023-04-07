from pydantic import BaseModel  # to create schema, so we have an idea what data we expect from the requests/responses
from datetime import datetime
from pydantic import EmailStr
from typing import Optional


class PostBase(BaseModel):
    post_title: str
    post_content: str
    post_published: bool = True


class PostCreate(PostBase):
    pass


class UserResponse(BaseModel):
    user_id: int
    user_email: EmailStr
    user_created_at: datetime

    class Config:
        orm_mode = True


class PostResponse(PostBase):
    post_id: int
    post_created_at: datetime
    owner: UserResponse

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    post: PostResponse
    n_votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    user_email: EmailStr
    user_password: str


class UserLogin(BaseModel):
    user_email: EmailStr
    user_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    vote_dir: bool
