from database.models import *
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import Session


def all_rating_db():
    engine = create_engine('sqlite:///repbot.db', echo=False, connect_args={'check_same_thread': False})
    db = Session(bind=engine)
    students = db.query(Rating).order_by(desc(Rating.points)).all()
    try:
        all_students = [[info.user_name, info.points] for info in students]
        return all_students
    except:
        return []