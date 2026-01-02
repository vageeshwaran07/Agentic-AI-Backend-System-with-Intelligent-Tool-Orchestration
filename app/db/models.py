from sqlalchemy import Column, Integer, String, Date
from app.db.session import Base

class Meeting(Base):
    __tablename__ = "meetings"

    id =Column(Integer, primary_key=True, index= True)
    title = Column(String, nullable = False)
    date = Column(Date, nullable = False)
