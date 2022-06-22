from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from .database import Base


class Record(Base):
    __tablename__ = "prices"
    date = Column(Date, primary_key=True)
    ticker = Column(String(255), primary_key=True)
    price = Column(Integer)
    volume = Column(Integer)
    recoveries = Column(Integer)
