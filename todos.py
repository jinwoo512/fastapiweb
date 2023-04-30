from fastapi import APIRouter
from model import Todo

todo_router = APIRouter()

todo_list = []

# @router.get("/hello")
# async def say_hello() -> dict:
#     return {
#         "message": "hello world"
#     }

@todo_router.post("/todo") # 데이터 넣을 때는 post
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo added successfully."
    }

@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {
        "todos": todo_list
    }

@todo_router.get("/todo/{todo_id}") # 매개변수로 받기
async def get_single_todo(todo_id: int) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    return {
        "message": "Todo with supplied ID doesn't exist."
    }