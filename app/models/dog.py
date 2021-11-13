from app.models.pet import Pet


class Dog(Pet):
    def __init__(self, name):
        super(Dog, self).__init__(name=name)
