from collections.abc import Generator
from typing import Annotated
from fastapi import Header
from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import Session

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_size=30,        
    max_overflow=50,     
    pool_timeout=60,     
    pool_recycle=1800,   
    pool_pre_ping=True
)

def get_db():
    import app.models.service_config
    with Session(engine) as session:
        yield session
        
# Sau khi định nghĩa xong get_db thì mới dùng đến nó
SessionDep = Annotated[Session, Depends(get_db)]