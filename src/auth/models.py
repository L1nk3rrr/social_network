from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.ext.declarative import declarative_base


AuthBase = declarative_base()


class User(SQLAlchemyBaseUserTable[int], AuthBase):
    id: int = Column(Integer, primary_key=True)
    username: str = Column(String, nullable=False)
    last_login: datetime = Column(DateTime(timezone=True), nullable=True)
    last_request: datetime = Column(DateTime(timezone=True), nullable=True)
