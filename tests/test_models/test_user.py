#!/usr/bin/python3
"""Module with unittest"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models.base_model import BaseModel
import os


class test_User(test_basemodel):
    """Class with tests"""

    def __init__(self, *args, **kwargs):
        """Initializing"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_first_name(self):
        """Testign first name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_last_name(self):
        """Testing last name"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_email(self):
        """Testing email"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_password(self):
        """Testing passowrd"""
        new = self.value()
        self.assertEqual(type(new.password), str)


if __name__ == "__main__":
    unittest.main()
