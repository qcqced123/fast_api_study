import datetime
from pydantic import BaseModel, validator
from ..answer.answer_schema import Answer

# Question Schema
class Question(BaseModel):
  id: int
  subject: str
  # subject: str | None = None
  content: str
  create_date: datetime.datetime
  answers: list[Answer] = [] # Question & Answer Mapping
  # Question Model이 자동으로 Question Schema로 변환되도록 하는 기능
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

