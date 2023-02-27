from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Make Data Scheme with Python Class
class Question(Base):
  __tablename__ = "question"

  id = Column(Integer, primary_key=True) # primary_key: setting id to database's unique key values
  subject = Column(String, nullable=False) # if false, you cannot blank or nan value in subject column
  content = Column(Text, nullable=False)
  create_date = Column(DateTime, nullable=False)

class Answer(Base):
  __tablename__ = "answer"

  id = Column(Integer, primary_key=True) # primary_key: setting id to database's unique key values
  content = Column(Text, nullable=False)
  create_date = Column(DateTime, nullable=False)
  question_id = Column(Integer, ForeignKey("question.id"))
  question = relationship("Question", backref="answers") # backref => Very Important
