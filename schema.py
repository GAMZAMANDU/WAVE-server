from pydantic import BaseModel, Field
from typing import Optional


# ✅ 사용자 생성 요청 스키마
class UserCreate(BaseModel):
    name: str = Field(..., max_length=255, description="사용자 이름")
    password: str = Field(..., max_length=255, description="사용자 비밀번호")


# ✅ 사용자 응답 스키마 (비밀번호 제외)
class UserOut(BaseModel):
    id: int  # 사용자 ID
    name: str  # 사용자 이름

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    name: str = Field(..., max_length=255, description="사용자 이름")
    password: str = Field(..., max_length=255, description="사용자 비밀번호")

class HandleOut(BaseModel):
    id: int
    controles: str

class UserLoginOut(BaseModel):
    id: int  # 사용자 ID
    name: str  # 사용자 이름
    handle_config: list[HandleOut]

    class Config:
        orm_mode = True