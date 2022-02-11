from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class Lead(db.Model):

    __tablename__ = "leads"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    email: str = Column(String, nullable=False, unique=True)
    phone: str = Column(String, nullable=False, unique=True)
    creation_date: str = Column(DateTime, default=datetime.now())
    last_visit: str = Column(DateTime, default=datetime.now())
    visits: int = Column(Integer, nullable=True, default=1)

    def __repr__(self):
        return f"<[{self.id}]{self.name}>"

    def serializer(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "creation_date": self.creation_date,
            "last_visit": self.last_visit,
            "visits": self.visits,
        }
