from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from orm.models import base


class Student(base.get_base()):
    pass
