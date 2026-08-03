from fastapi import FastAPI
from fastapi import HTTPException
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome, I am Stephen"}

@app.get("/health_status")
def read_status():
    return {
        "status": "healthy",
        "active_model": "Steph 001",
        "gpu_available": False
    }

tasks = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Walk the dog", "done": False},
    {"id": 3, "title": "Write code", "done": True},
]

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for t in tasks:
        if t["id"] == task_id:
            return t
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

@app.put("/tasks/{task_id}")
def update_task(task_id: int, update: TaskUpdate):
    for t in tasks:
        if t["id"] == task_id:
            if update.title is not None:
                if not update.title.strip():
                    raise HTTPException(status_code=400, detail="Title cannot be empty")
                t["title"] = update.title
            if update.done is not None:
                t["done"] = update.done
            return t
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks.pop(i)
            return
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")