from typing import List, Dict, Union, Any
from pydantic import BaseModel, Field
from typing import Optional

# handler config에 대한 객체
class HandlerConfig(BaseModel):
    hand_id: int
    name: str
    icon: str
    content: Dict[int, Union[str, None]]

# /users에 사용되는 require용 객체
class UserCreate(BaseModel):
    name: str
    password: str
    handler_config: List[HandlerConfig] = []

# /users에 사용되는 resepone용 객체
class UserRes(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

# /login에 사용되는 require용 객체
class UserLogin(BaseModel):
    name: str = Field(..., max_length=255, description="사용자 이름")
    password: str = Field(..., max_length=255, description="사용자 비밀번호")

# /login에 사용되는 response용 객체
class UserLoginRes(BaseModel):
    id: int
    name: str
    handler_config: List[HandlerConfig]
    access_token : str

    class Config:
        orm_mode = True

# jwt token을 verify하기 위한 객체
class JWTverify(BaseModel):
    access_token: str
    name: str

# /run에 사용되는 response용 객체
class runRes (BaseModel):
    handler_config : List[HandlerConfig]

    class Config:
        orm_mode = True

