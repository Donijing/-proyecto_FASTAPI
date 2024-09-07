from fastapi import FastAPI ,HTTPException 
from database import get_all_tasks,create_task
from models import Task

app = FastAPI()

@app.get("/")

def home():
    return {"url":"hola estas en el inicio"}


@app.get("/home/tasks")

async def all():
    tasks = await get_all_tasks()
    return tasks

@app.post("/home/tasks")

async def c_tasks(task:Task):
    response = await create_task(task.dict())
    if response :
        print(response)
    raise HTTPException(400, 'something went wrong' )

@app.get('/home/tasks/{id}')

async def s_tasks():
    return "task this"

@app.put('/home/tasks/{id}')

async def u_tasks():
    return "task update"

@app.delete('/home/tasks/{id}')

async def d_tasks():
    return "task delete"

