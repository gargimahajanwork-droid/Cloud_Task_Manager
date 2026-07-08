from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db

from models import Task

from schemas import TaskSchema
# connects to neon and checks whether the tasks table exists , if not then create it 
Base.metadata.create_all(bind = engine)

# here base contains all the database table definitions
# and engine contains the cloud database connection \\

app = FastAPI()

@app.get("/")
def home():

    return {"message":"welcome to cloud task manager API"}
# this api tells that" FAstapi is running and the application started successfully 


# as per day 2 
@app.post("/create_task")
def create_task (task: TaskSchema, db:Session = Depends(get_db)):

    new_task = Task(task_title = task.task_title, description = task.description, assigned_to = task.assigned_to, priority = task.priority, status = task.status,due_date= task.due_date, created_by = task.created_by)

    
    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    return {"message":"Task created successfully"}

# the data from postman is first validated by the taskSchema (Pydantic schema ), if it is valid , the values 
# are then copied into the task model , which repsents the database table and finally stored in the database

@app.get("/tasks")
def view_task( db: Session = Depends(get_db)):

    tasks= db.query(Task).all()

    return tasks
