from fastapi import FastAPI
from todos import todo_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict: # async: 비동기처리 // '-> dict' 리턴 형식 지정
        return {
            "message": "Hello world"
        }

app.include_router(todo_router)