# from pydantic import BaseModel
# from typing import Optional

# class Task(BaseModel):
#     id: Optional[str]
#     title: str
#     descripcion:Optional[str] = None
#     completed:bool = False
    
from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    id:Optional[str] = None
    title: str
    description: Optional[str] = None
    completed: bool = False
