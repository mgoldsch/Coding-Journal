from app.models.family_member import FamilyMember
from app.models.pet import Pet


class Cat(Pet, FamilyMember):
    def __init__(self, name):
        super(Cat, self).__init__(name=name, greeting="meow")
