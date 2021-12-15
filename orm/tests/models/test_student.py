import pytest
from orm.models.student import Student

class TestStudent:
    def test_display_name(self):
        s = Student("First", "Last", 2022)
        assert s.display_name() == "First L."