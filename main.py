from app.models.dog import Dog
from app.models.family import Family
from app.models.kid import Kid
from app.models.parent import Parent

kid1 = Kid("Joe")
parent1 = Parent("Mom")
parent2 = Parent("Dad")
dog = Dog("Dog")

family_members = [kid1, parent1, parent2, dog]
family_name = "LastName"

test_family = Family(family_name, family_members)
print(test_family.get_members_names([Dog]))


