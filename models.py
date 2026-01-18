from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Url(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    original_url: str = Field(nullable=False)
    short_code: str = Field(index=True, nullable=False, unique=True, max_length=10)
    access_count: int = Field(default=0, nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

def create_db(engine):
    SQLModel.metadata.create_all(engine)
