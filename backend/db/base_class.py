from typing import Any 
from sqlalchemy.ext.declarative import as_declarative,declared_attr

@as_declarative()
class Base:
    id : Any
    _name_: str

    def _tablename_(cls)->str:
        return cls._name_.lower()