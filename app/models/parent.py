from app.models.family_member import FamilyMember
from app.models.person import Person


class Parent(Person, FamilyMember):
    def __init__(self, name):
        super(Parent, self).__init__(name=name, greeting="Hello")
