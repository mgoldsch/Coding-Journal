from orm.models import base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from orm.models.student import Student

Base = base.get_base()

session = sessionmaker()
engine = create_engine("sqlite:///database/orm.sqlite")
session.configure(bind=engine)

Base.metadata.create_all(engine)

ses = session()