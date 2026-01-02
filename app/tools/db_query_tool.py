from datetime import date, timedelta
from app.db.session import SessionLocal
from app.db.models import Meeting


def get_meetings_for_date(target_date):
    db = SessionLocal()
    meetings = db.query(Meeting).filter(Meeting.date == target_date).all()
    db.close()
    return meetings


def get_meetings_between(start_date, end_date):
    db = SessionLocal()
    meetings = (
        db.query(Meeting)
        .filter(Meeting.date >= start_date, Meeting.date <= end_date)
        .all()
    )
    db.close()
    return meetings


def get_all_meetings():
    db = SessionLocal()
    meetings = db.query(Meeting).all()
    db.close()
    return meetings
