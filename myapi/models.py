from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Make Data Model with Python Class
# Question Model
class Question(Base):
  __tablename__ = "question"

  id = Column(Integer, primary_key=True) # primary_key: setting id to database's unique key values
  subject = Column(String, nullable=False) # if false, you cannot blank or nan value in subject column
  content = Column(Text, nullable=False)
  create_date = Column(DateTime, nullable=False)

# Answer Model
class Answer(Base):
  __tablename__ = "answer"

  id = Column(Integer, primary_key=True) # primary_key: setting id to database's unique key values
  content = Column(Text, nullable=False)
  create_date = Column(DateTime, nullable=False)
  question_id = Column(Integer, ForeignKey("question.id"))
  question = relationship("Question", backref="answers") # backref => Very Important


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)



