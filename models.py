from typing import Optional
from pydantic import BaseModel


class Boss(BaseModel):
    id: Optional[int] = None
    name: str
    title: str
    location: str
    drops: int
    shardbearer: bool
    
     