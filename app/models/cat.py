from app.models.pet import Pet


class Cat(Pet):
    def __init__(self, name):
        super(Cat, self).__init__(name=name)
