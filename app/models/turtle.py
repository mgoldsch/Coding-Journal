from app.models.pet import Pet


class Turtle(Pet):
    def __init__(self, name):
        super(Turtle, self).__init__(name=name)
