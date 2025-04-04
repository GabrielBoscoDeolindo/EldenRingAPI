from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import BaseModel

class Boss(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str 
    photo: str
    description: str

class BossUpdate(BaseModel):
    name: Optional[str] = None
    photo: Optional[str] = None
    description: Optional[str] = None

def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)
