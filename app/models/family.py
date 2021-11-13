class Family:
    def __init__(self, family_name, family_members):
            self.family_name = family_name
            self.family_members = family_members

    def add_member(self, member):
        self.family_members.append(member)

    def remove_member(self, member):
        self.family_members.remove(member)

    def get_members(self, filters = None):
        if filters is None:
            return self.family_members
        else:
            members = []
            for member in self.family_members:
                for filter in filters:
                    if isinstance(member, filter):
                        members.append(member)
            return members
        