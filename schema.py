from typing import List, Dict, Union, Any
from pydantic import BaseModel, Field
from typing import Optional

class HandlerConfig(BaseModel):
    hand_id: int
    name: str
    icon: str
    content: Dict[int, Union[str, None]]

class UserCreate(BaseModel):
    name: str
    password: str
    handler_config: List[HandlerConfig] = []


class UserOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    name: str = Field(..., max_length=255, description="사용자 이름")
    password: str = Field(..., max_length=255, description="사용자 비밀번호")


class UserLoginOut(BaseModel):
    id: int
    name: str
    handler_config: List[HandlerConfig] = []
    access_token : str

    class Config:
        orm_mode = True



