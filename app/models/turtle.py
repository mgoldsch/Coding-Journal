from app.models.family_member import FamilyMember
from app.models.pet import Pet


class Turtle(Pet, FamilyMember):
    def __init__(self, name):
        super(Turtle, self).__init__(name=name, greeting="...")
