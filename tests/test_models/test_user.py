#!/usr/bin/python3
"""Module with unittest"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models.base_model import BaseModel
import os


class test_User(test_basemodel):
    """Class with tests"""

    @classmethod
    def setUpClass(cls):
        """Setting up"""
        cls.user = User()
        cls.user.first_name = "First"
        cls.user.last_name = "Last"
        cls.user.email = "email@mail.com"
        cls.user.password = "passwd"

    @classmethod
    def teardown(cls):
        """Tearing down"""
        del cls.user


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

    def test_attributes_user(self):
        """Testing attributes"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_attribute_types_user(self):
        """Testing types"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_save_user(self):
        """Testing save"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_user(self):
        """Testing dict"""
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
