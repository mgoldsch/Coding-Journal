from sqlalchemy import Column, String, Integer
from models.base import *

class College(Base):
    __tablename__ = 'colleges'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, students):
        self.students = students