from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from models import base


class Student(base.get_base()):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    class_year = Column(Integer)

    def __init__(self, first_name, last_name, class_year):
        self.first_name = first_name
        self.last_name = last_name
        self.class_year = class_year