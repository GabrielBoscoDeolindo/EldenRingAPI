from typing import Optional
from sqlmodel import SQLModel, Field

class Boss(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str 
    photo: str
    description: str

def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)
