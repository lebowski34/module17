from fastapi import APIRouter
from app.schemas import CreateTask, UpdateTask

task_router = APIRouter(
    prefix="/task",
    tags=["task"],
)

@task_router.get("/")
async def all_tasks():
    # TODO: Implement logic to retrieve all tasks
    return {"message": "Get all tasks"}

@task_router.get("/{task_id}")
async def task_by_id(task_id: int):
    # TODO: Implement logic to retrieve a task by ID
    return {"message": "Get task by ID"}

@task_router.post("/create")
async def create_task(task: CreateTask):
    # TODO: Implement logic to create a new task
    return {"message": "Create a new task"}

@task_router.put("/update")
async def update_task(task_id: int, task: UpdateTask):
    # TODO: Implement logic to update an existing task
    return {"message": "Update a task"}

@task_router.delete("/delete")
async def delete_task(task_id: int):
    # TODO: Implement logic to delete a task
    return {"message": "Delete a task"}