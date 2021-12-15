from models.base import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models.student import Student
from models.college import College

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
students = []
students.append(student)
college = College(students)
ses.add(college)
college.name = "test"
ses.commit()

students = ses.query(Student).all()
for s in students:
    print(f"student: {s.first_name}, {s.last_name}, {s.class_year}")

retrieve_class_year = int(input("Please enter the class year of students you would like to query: "))
students = ses.query(Student).filter(Student.class_year == retrieve_class_year)
for s in students:
    print(f"student: {s.display_name()}, {s.first_name}, {s.last_name}, {s.class_year}, {s.college.name}")