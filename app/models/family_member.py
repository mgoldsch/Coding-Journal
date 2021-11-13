class FamilyMember:
    def __init__(self, greeting):
        self.family_name = ""
        self.greeting = greeting

    def trigger_greeting(self):
        print(self.greeting)
        