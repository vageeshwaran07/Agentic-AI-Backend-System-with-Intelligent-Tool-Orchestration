from datetime import date
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import Meeting


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def meeting_exists(meeting_date: date):
    db = SessionLocal()
    meeting = db.query(Meeting).filter(Meeting.date == meeting_date).first()
    db.close()
    return meeting


def create_meeting(title: str, meeting_date: date):
    db = SessionLocal()
    meeting = Meeting(title=title, date=meeting_date)
    db.add(meeting)
    db.commit()
    db.refresh(meeting)
    db.close()
    return meeting
