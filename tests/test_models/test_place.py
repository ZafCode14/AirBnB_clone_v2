#!/usr/bin/python3
"""Module with unittest"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import os


class test_Place(test_basemodel):
    """Class with tests"""

    def __init__(self, *args, **kwargs):
        """Initializing"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_city_id(self):
        """Testing city id"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_user_id(self):
        """Testign user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_name(self):
        """Testign name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_description(self):
        """Testing description"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_number_rooms(self):
        """Testing number of rooms"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_number_bathrooms(self):
        """Testing number of bathrooms"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_max_guest(self):
        """Testign number of max guests"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_price_by_night(self):
        """Testign price"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_latitude(self):
        """Testing lat"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_longitude(self):
        """Testing lon"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_amenity_ids(self):
        """Testign amenity ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()
