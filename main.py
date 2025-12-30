from fastapi import FastAPI,Depends
from model import *
from schemas import *
import uvicorn 
from sqlalchemy.orm import Session 
from database import *

Base.metadata.create_all(bind=engine)
app=FastAPI()

@app.get('/')
async def home():
    return {'message':'welcome to loading env files'}


@app.post('/new',response_model=TodoBase)
async def create_todo(todo:TodoCreate,db:Session=Depends(connect)):
    new_todo=Todo(title=todo.title,description=todo.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo 

@app.get('/all',response_model=list[TodoBase])
async def get_all_todos(db:Session=Depends(connect)):
    return db.query(Todo).all() 


@app.get('/{id}',response_model=TodoBase)
async def get_todo(id:int,db:Session=Depends(connect)):
    return db.query(Todo).filter(Todo.id==id).first()