from pydantic import BaseModel, validator
from domain.user.user_schema import User
import datetime
from datetime import datetime

class AnswerCreate(BaseModel):
    content: str # dataclasses wrapper가 들어가 있는 듯
    @validator('content')
    def not_empty(cls, v): # 이미 dataclasses wrapper: self 선언 굳이 필요 없음
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


# 1 Answer schema for print
class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime
    user: User | None
    question_id: int
    modify_date: datetime.datetime | None = None


    class Config:
        orm_mode = True


class AnswerUpdate(AnswerCreate):
    answer_id: int


class AnswerDelete(BaseModel):
    answer_id: int


