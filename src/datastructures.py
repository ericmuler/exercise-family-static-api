
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self.last_name = last_name
        self._next_id = 1
        self._members = []


    def _generate_id(self):
        return randint(0, 99999999)

    def add_member(self, member):

        if 'id' not in member:
            member['id'] = self._generate_id()

        member['last_name'] = self.last_name

        self._members.append(member)

        return self._members


    def delete_member(self, id):
        
        for i, member in enumerate(self._members):
            if member['id'] == id:
                del self._members[i]
                return True
        return False


    def get_member(self, id):

        for member in self._members:
            if member['id'] == id:
                return member
        return None

    def get_all_members(self):
        return self._members