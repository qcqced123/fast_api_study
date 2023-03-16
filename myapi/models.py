from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Make Data Model with Python Class
# Question Model
question_voter = Table(
    'question_voter',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('question_id', Integer, ForeignKey('question.id'), primary_key=True)
)


class Question(Base):
  __tablename__ = "question"

  id = Column(Integer, primary_key=True) # primary_key: setting id to database's unique key values
  subject = Column(String, nullable=False) # if false, you cannot blank or nan value in subject column
  content = Column(Text, nullable=False)
  create_date = Column(DateTime, nullable=False)
  user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
  user = relationship("User", backref="question_users")
  modify_date = Column(DateTime, nullable=True)

# Answer Model
answer_voter = Table(
    'answer_voter',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('answer_id', Integer, ForeignKey('answer.id'), primary_key=True)
)

class Answer(Base):
  __tablename__ = "answer"

  id = Column(Integer, primary_key=True) # primary_key: setting id to database's unique key values
  content = Column(Text, nullable=False)
  create_date = Column(DateTime, nullable=False)
  question_id = Column(Integer, ForeignKey("question.id"))
  question = relationship("Question", backref="answers") # backref => Very Important
  user_id = Column(Integer, ForeignKey("user.id"), nullable=True) # add user info
  user = relationship("User", backref="answer_users") # add user info
  modify_date = Column(DateTime, nullable=True)
  voter = relationship('User', secondary=answer_voter, backref='answer_voters')


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)



