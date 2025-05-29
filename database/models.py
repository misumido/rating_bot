from sqlalchemy import (Column, Integer,
                        String, DateTime, Float)
from database import Base

class Rating(Base):
    __tablename__ = "rating"
    user_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_name = Column(String, unique=True)
    points = Column(Float, default=0.0)
    reg_date = Column(DateTime)

class Statistic(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String)
    points = Column(Float, default=0.0)
    points_cat = Column(String, default="other")
    reg_date = Column(DateTime)






