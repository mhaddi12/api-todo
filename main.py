""" To-Do API """
# To-Do API using FastAPI
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
api_store_list = []


class Task(BaseModel):
    """
    Represents a task with a description and completion status.

    Attributes:
        task (str): The description of the task.
        completed (bool): Whether the task is completed.
    """
    task: str
    completed: bool = False


@app.post("/api/store")
async def create_post(task: Task):
    """
    Create a new task and add it to the API store.

    Args:
        task (Task): The task to create.

    Returns:
        dict: A dictionary containing a success message and the created task.
    """
    api_store_list.append(task.task)
    return {"message": "Task added successfully", "task": task.task}


@app.get("/api/store")
async def get_tasks():
    """
    Retrieve all tasks stored in the API.

    Returns:
        dict: A dictionary containing a list of all tasks under the key 'tasks'.
    """

    return {"tasks": api_store_list}


@app.get("/api/store/{task_id}")
async def get_task_by_id(task_id: int):
    """
    Retrieve a task by its ID.

    Args:
        task_id (int): The ID of the task to retrieve.

    Returns:
        dict: A dictionary containing the task, or an error message if the task is not found.
    """
    if task_id < len(api_store_list):
        return {"task": api_store_list[task_id]}
    else:
        return {"error": "Task not found"},


@app.put("/api/store/{task_id}")
async def update_task(task_id: int, task: Task):
    """
    Update a task by its ID.

    Args:
        task_id (int): The ID of the task to update.
        task (Task): The updated task.

    Returns:
        dict: A dictionary containing a success message and the updated task, or an error message if the task is not found.
    """

    if task_id < len(api_store_list):
        api_store_list.insert(task_id, task.task)
        return {"message": "Task updated successfully", "task": task.task}
    else:
        return {"error": "Task not found"}


@app.delete("/api/store/{task_id}")
async def delete_task(task_id: int):
    """
    Delete a task by its ID.

    Args:
        task_id (int): The ID of the task to delete.

    Returns:
        dict: A dictionary containing a success message and the deleted task, or
            an error message if the task is not found.
    """

    if (task_id < len(api_store_list)):
        deleted_task = api_store_list.pop(task_id)
        return {"message": "Task deleted successfully", "task": deleted_task}
    else:
        return {"error": "Task not found"}


@app.get("/")
async def read_root():
    """
    Returns a welcome message for the To-Do API.

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"message": "Welcome to the To-Do API!"}
