class Person:
    def __init__(self, first_name, last_name=None, preferred_name=None, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.preferred_name = preferred_name

    def full_name(self):
        if self.preferred_name is None:
            return self.first_name + " " + self.last_name
        else:
            return self.preferred_name + " " + self.last_name
