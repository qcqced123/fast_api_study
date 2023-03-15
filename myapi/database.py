import contextlib
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Address for DataBase: save sqlite3 file in root directory
SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

# Rule 1
"""
[fuction]
1) create_engine()
  - create connection pool: control the number of session which is entered DataBase, minimize entering time
"""
engine = create_engine(
  SQLALCHEMY_DATABASE_URL,
  connect_args={'check_same_thread': False},
)

# Class used to enter DataBase
"""
[parameter]
1) autocommit: bool type
  - True: save automatic change point, but cannot rollback change point
  - False: if you want to apply change point, you should write down 'commit' to terminal, also can rollback
"""
SessionLocal = sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=engine,
)

# Rule 2
Base = declarative_base()
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
Base.metadata = MetaData(naming_convention=naming_convention)

# DataBase Generator
# db: Session = Depends(get_db) => True, remove @contextlib.contextmanager
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
