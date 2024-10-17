from sqlalchemy import Column, Integer, String, JSON

from ..database import Base

class Template(Base):
    __tablename__ = "templates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    content = Column(JSON)
