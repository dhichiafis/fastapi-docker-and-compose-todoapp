from pydantic import BaseModel,ConfigDict
from datetime import datetime
class TodoCreate(BaseModel):
    title:str 
    description:str 

class TodoBase(TodoCreate):
    id:int 
    created_at:datetime
    model_config=ConfigDict(from_attributes=True)