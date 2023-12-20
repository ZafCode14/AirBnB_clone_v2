#!/usr/bin/python3
"""Module with a unittest"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import os
import pep8


class test_City(test_basemodel):
    """Class with tests"""

    @classmethod
    def setUpClass(cls):
        """Setting up"""
        cls.city = City()
        cls.city.name = "City Name"
        cls.city.state_id = "State Name"

    @classmethod
    def teardown(cls):
        """Tearing down"""
        del cls.city

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/amenity.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def __init__(self, *args, **kwargs):
        """Initializing"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_state_id(self):
        """Testing state id"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_name(self):
        """Testign name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
    
    def test_attributes_city(self):
        """Testing for attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_attribute_types_city(self):
        """Testing for attr types"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)


if __name__ == "__main__":
    unittest.main()
