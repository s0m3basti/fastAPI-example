from fastapi import FastAPI

from app.server.routes.student import router as StudentRouter

# run via uvicorn app.server.app:app --reload

# app is fastAPI
app = FastAPI()

# include te routes from students
app.include_router(StudentRouter, tags=["Student"], prefix="/student")

# basic rout and function 
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this super app!"}