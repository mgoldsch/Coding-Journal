class Person:
    def __init__(self, first_name, last_name, preferred_name, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.preferred_name = preferred_name

    def full_name(self):
        if self.preferred_name != "":
            return self.preferred_name + " " + self.last_name
        else:
            return self.first_name + " " + self.last_name
        