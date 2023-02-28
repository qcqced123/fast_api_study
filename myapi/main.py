from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from domain.question import question_router

# same as flask
app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router((question_router.router)) # admin question_router's router in app