from sqlalchemy import Column,Integer,ForeignKey,String,DateTime
from datetime import datetime
from database import *

class Todo(Base):
    __tablename__='todos'
    id=Column('id',Integer,primary_key=True)
    title=Column('title',String)
    description=Column('description',String)
    created_at=Column('created_at',DateTime,default=datetime.now)



