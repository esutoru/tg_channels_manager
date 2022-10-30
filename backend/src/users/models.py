from sqlalchemy import Boolean, Column, Integer, String

from backend.src.database.core import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    is_active = Column(Boolean, default=True)