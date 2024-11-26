from sqlalchemy.orm import Session
from ..repositories import task_repo
from .. import schemas

def get_tasks(db: Session):
    return task_repo.get_tasks(db)

def create_task(db: Session, task: schemas.TaskCreate):
    return task_repo.create_task(db, task)
