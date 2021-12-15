from models import base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models.student import Student

Base = base.get_base()

session = sessionmaker()
engine = create_engine("sqlite:///database/orm.sqlite")
session.configure(bind=engine)

Base.metadata.create_all(engine)

ses = session()

print("You will enter a students info....")
first_name = input("Please enter the student's first name: ")
last_name = input("Please enter the student's last name: ")
class_year = int(input("Please enter the student's class year: "))

student = Student(first_name, last_name, class_year)

ses.add(student)
ses.commit()

students = ses.query(Student).all()
for s in students:
    print(f"student: {s.first_name}, {s.last_name}, {s.class_year}")