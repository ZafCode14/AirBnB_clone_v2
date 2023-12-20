#!/usr/bin/python3
"""Module with unittest"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import os


class test_Place(test_basemodel):
    """Class with tests"""

    @classmethod
    def setUpClass(cls):
        """Setting up"""
        cls.place = Place()
        cls.place.city_id = "testing-the-id"
        cls.place.user_id = "testing-the-id"
        cls.place.name = "Cool Place"
        cls.place.description = "Some description"
        cls.place.number_rooms = 1
        cls.place.number_bathrooms = 1
        cls.place.max_guest = 2
        cls.place.price_by_night = 30
        cls.place.latitude = 23.8
        cls.place.longitude = 83.9
        cls.place.amenity_ids = ["testing-the-id"]

    @classmethod
    def teardown(cls):
        """Tearing down"""
        del cls.place

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

    def test_attributes_place(self):
        """Testing for attributes"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_attribute_types_place(self):
        """Testing for attr types"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_save_city(self):
        """Testing save"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict_city(self):
        """Testing to dict"""
        self.assertEqual('to_dict' in dir(self.place), True)



if __name__ == "__main__":
    unittest.main()
