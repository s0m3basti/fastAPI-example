from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.server.routes.student import router as StudentRouter

# run via uvicorn app.server.app:app --reload

# app is fastAPI
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include te routes from students
app.include_router(StudentRouter, tags=["Student"], prefix="/student")

# basic rout and function 
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this super app!"}