from app.models.family_member import FamilyMember
from app.models.pet import Pet


class Dog(Pet, FamilyMember):
    def __init__(self, name):
        super(Dog, self).__init__(name=name, greeting="woof")
