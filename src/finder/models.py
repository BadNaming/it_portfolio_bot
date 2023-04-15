from sqlalchemy import Column, Date, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Participant(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    spec = Column(String(100))
    exp = Column(String(100))
    available = Column(String(100))
    worktime = Column(String(100))
    education = Column(String(100))
    city = Column(String(100))
    wants = Column(Text)
    can_do = Column(Text)
    tg_nickname = Column(String(100))
    accept = Column(String(10))
    timezone = Column(String(10))


class Search(Base):
    __tablename__ = 'search'

    id = Column(Integer, primary_key=True)
    user = Column(String(100))
    spec = Column(String(100))
    exp = Column(String(100))