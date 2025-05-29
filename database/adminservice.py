from database.models import *
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import Session
from datetime import datetime
import pytz
tashkent_timezone = pytz.timezone('Asia/Tashkent')

def add_student_db(name):
    engine = create_engine('sqlite:///repbot.db', echo=False, connect_args={'check_same_thread': False})
    db = Session(bind=engine)
    new_student = Rating(user_name=name, reg_date=datetime.now(tashkent_timezone))
    db.add(new_student)
    db.commit()

def all_students_db():
    engine = create_engine('sqlite:///repbot.db', echo=False, connect_args={'check_same_thread': False})
    db = Session(bind=engine)
    students = db.query(Rating).order_by(desc(Rating.points)).all()
    try:
        all_students = [info.user_name for info in students]
        return all_students
    except:
        return []
def add_points_db(name, points):
    engine = create_engine('sqlite:///repbot.db', echo=False, connect_args={'check_same_thread': False})
    db = Session(bind=engine)
    student = db.query(Rating).filter_by(user_name=name).first()
    if student:
        student.points += float(points)
        db.commit()
    else:
        pass
def minus_points_db(name, points):
    engine = create_engine('sqlite:///repbot.db', echo=False, connect_args={'check_same_thread': False})
    db = Session(bind=engine)
    student = db.query(Rating).filter_by(user_name=name).first()
    if student:
        student.points -= float(points)
        db.commit()
    else:
        pass

