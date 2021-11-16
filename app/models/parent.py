from app.models.family_member import FamilyMember
from app.models.person import Person


class Parent(Person, FamilyMember):
    def __init__(self, first_name, last_name=None, preferred_name=None):
        super(Parent, self).__init__(first_name=first_name, last_name=last_name,
                                     preferred_name=preferred_name, greeting="Hello")
