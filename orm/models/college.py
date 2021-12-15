from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from models import base

class College(base.get_base()):
    __tablename__ = 'colleges'
    id = Column(Integer, primary_key=True)
    name = Column(String)