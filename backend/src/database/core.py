from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

from backend.src.config import settings
from backend.src.database.utils import resolve_table_name

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@as_declarative()
class Base:
    __name__: str

    @declared_attr
    def __tablename__(self) -> str:
        return resolve_table_name(self.__name__)
