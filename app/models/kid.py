from app.models.family_member import FamilyMember
from app.models.person import Person


class Kid(Person, FamilyMember):
    def __init__(self, name):
        super(Kid, self).__init__(first_name=name, greeting="Hey!")