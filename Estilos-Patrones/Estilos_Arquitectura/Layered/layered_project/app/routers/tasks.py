from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..services import task_service
from .. import schemas
from ..database import get_db

router = APIRouter()

@router.get("/tasks", response_model=list[schemas.Task])
def read_tasks(db: Session = Depends(get_db)):
    return task_service.get_tasks(db)

@router.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task(db, task)
