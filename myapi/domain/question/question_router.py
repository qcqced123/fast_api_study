from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from ..question import question_schema, question_crud
from database import SessionLocal
from database import get_db
from domain.user.user_router import get_current_user
from models import User

# Must init router object
"""
prefix:
  - '/api/question' 으로 시작 되는 요청이 올 때, 해당 값의 prefix를 갖는 파일의 특정 함수가 실행 되게 하는 기능
  - 여기서는 question_list 함수에 router.get을 list로 달아뒀기 때문에 /api/question/list라는 요청이 오면 question_router 파일의
  - question_list Function execute
"""
router = APIRouter(
  prefix='/api/question',
)

# @router.get('/list')
# def question_list():
#   db = SessionLocal()
#   _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#   db.close() # return session to connection pool
#   return _question_list


"""
db: Session = Depends(get_db)
  - Session Generator에 의해 생성된 Session Object가 DB Object에 주입
response_model=list[question_schema.Question]
  - question_list의 리턴값이 Question Schema로 구성된 리스트임을 명시
"""


@router.get("/list", response_model=question_schema.QuestionList)
def question_list(db: Session = Depends(get_db),
                  page: int = 0, size: int = 10):
    total, _question_list = question_crud.get_question_list(
        db, skip=page*size, limit=size)
    return {
        'total': total,
        'question_list': _question_list
    }


@router.get('/detail/{question_id}', response_model=question_schema.Question)
def question_detail(question_id: int, db: Session=Depends(get_db)):
  question = question_crud.get_question(db, question_id=question_id)
  return question


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    question_crud.create_question(db=db,
                                  question_create=_question_create,
                                  user=current_user)


@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def question_update(_question_update: question_schema.QuestionUpdate,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_question = question_crud.get_question(db, question_id=_question_update.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_question.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="수정 권한이 없습니다.")
    question_crud.update_question(db=db, db_question=db_question,
                                  question_update=_question_update)


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def question_delete(_question_delete: question_schema.QuestionDelete,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_question = question_crud.get_question(db, question_id=_question_delete.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_question.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="삭제 권한이 없습니다.")
    question_crud.delete_question(db=db, db_question=db_question)


@router.post("/vote", status_code=status.HTTP_204_NO_CONTENT)
def question_vote(_question_vote: question_schema.QuestionVote,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    db_question = question_crud.get_question(db, question_id=_question_vote.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    question_crud.vote_question(db, db_question=db_question, db_user=current_user)