import datetime
from pydantic import BaseModel, validator
from ..answer.answer_schema import Answer
from domain.user.user_schema import User


# Question Schema
class Question(BaseModel):
  id: int
  subject: str
  # subject: str | None = None
  content: str
  create_date: datetime.datetime
  answers: list[Answer] = [] # Question & Answer Mapping
  user: User | None
  # Question Model이 자동으로 Question Schema로 변환되도록 하는 기능
  modify_date: datetime.datetime | None = None
  voter: list[User] = []

  class Config:
    orm_mode = True


class QuestionCreate(BaseModel):
    subject: str
    content: str

    @validator('subject', 'content') # same as __getattr__
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = []


# 질문에 대한 추천 개수 표시 기능
class QuestionVote(BaseModel):
    question_id: int


class QuestionUpdate(QuestionCreate):
    question_id: int


class QuestionDelete(BaseModel):
    question_id: int
