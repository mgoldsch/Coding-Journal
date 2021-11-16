import pytest

from app.models.person import Person


class TestPerson:

    def test_full_name(self):
        test_person = Person(first_name = 'Joe', last_name = 'Smith')
        assert test_person.full_name() == 'Joe Smith'

    def test_preferred_name(self):
        test_person = Person(first_name='Joe', last_name='Smith', preferred_name = 'Joey')
        assert test_person.full_name() == 'Joey Smith'
        