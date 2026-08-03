from sqlalchemy import Column, String, JSON
from app.database import Base

class DBItem(Base):
    __tablename__ = "items"

    id = Column(String, primary_key=True, index=True)
    content = Column(JSON)