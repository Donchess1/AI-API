from sqlalchemy.orm import Session
from .models import Item

class PostgresRepository:
    def __init__(self, db_session: Session):
        self.session = db_session

    def save_item(self, item_id: str, data: dict):
        db_item = Item(id=item_id, content=data)
        self.session.add(db_item)
        self.session.commit()