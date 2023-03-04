import datetime
from pydantic import BaseModel
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
