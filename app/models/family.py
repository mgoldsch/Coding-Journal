class Family:
    def __init__(self, family_name, family_members):
        self.family_name = family_name
        self.family_members = family_members
        for member in self.family_members:
            self._set_family_name(member)

    def add_member(self, member):
        self.family_members.append(member)
        self._set_family_name(member)

    def remove_member(self, member):
        self.family_members.remove(member)
        self._remove_family_name(member)

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

    def _set_family_name(self, member):
        member.family_name = self.family_name

    def _remove_family_name(self, member):
        member.family_name = ""
        