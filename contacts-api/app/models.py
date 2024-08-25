from sqlalchemy import Column, Integer, String, Date
from database import Base  # вставити свою бд

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    birthday = Column(Date)
    # додаткова інфа