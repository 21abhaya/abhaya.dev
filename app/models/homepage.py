from sqlalchemy import Table, Column, String, Integer, DateTime, Text
from sqlalchemy.orm import registry
from ..db.database import Base

class Homepage(Base):
    __tablename__ = "homepage"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    created_on = Column(DateTime, nullable=False)
    updated_on = Column(DateTime, nullable=False)


