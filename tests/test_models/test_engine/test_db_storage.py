#!/usr/bin/python3
"""Module with a class with unittest"""
import unittest
from os import getenv
import MySQLdb
from models.state import State
from models.engine.db_storage import DBStorage
import pep8
import models


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'Not db storage')
class TestDBStorage(unittest.TestCase):
    """Class with tests for DBstorage"""

    @classmethod
    def setUpClass(cls):
        """Setting up"""
        if type(models.storage) == DBStorage:
            cls.storage = DBStorage()
            Base.metadata.create_all(cls.storage._DBStorage__engine)
            Session = sessionmaker(bind=cls.storage._DBStorage__engine)
            cls.storage._DBStorage__session = Session()
            cls.state = State(name="California")
            cls.storage._DBStorage__session.add(cls.state)
            cls.city = City(name="San_Jose", state_id=cls.state.id)
            cls.storage._DBStorage__session.add(cls.city)
            cls.user = User(email="poppy@holberton.com", password="betty")
            cls.storage._DBStorage__session.add(cls.user)
            cls.place = Place(city_id=cls.city.id, user_id=cls.user.id,
                              name="School")
            cls.storage._DBStorage__session.add(cls.place)
            cls.amenity = Amenity(name="Wifi")
            cls.storage._DBStorage__session.add(cls.amenity)
            cls.review = Review(place_id=cls.place.id, user_id=cls.user.id,
                                text="stellar")
            cls.storage._DBStorage__session.add(cls.review)
            cls.storage._DBStorage__session.commit()

    @classmethod
    def tearDownClass(cls):
        """Tearing down"""
        if type(models.storage) == DBStorage:
            cls.storage._DBStorage__session.delete(cls.state)
            cls.storage._DBStorage__session.delete(cls.city)
            cls.storage._DBStorage__session.delete(cls.user)
            cls.storage._DBStorage__session.delete(cls.amenity)
            cls.storage._DBStorage__session.commit()
            del cls.state
            del cls.city
            del cls.user
            del cls.place
            del cls.amenity
            del cls.review
            cls.storage._DBStorage__session.close()
            del cls.storage

    def test_pep8(self):
        """Testign pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'Not db storage')
    def test_show(self):
        """Testing show"""
        self.query.execute("SHOW TABLES")
        result = self.query.fetchall()
        self.assertEqual(len(result), 7)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'Not db storage')
    def test_all_user(self):
        """Testing all from users"""
        self.query.execute("SELECT * FROM users")
        result = self.query.fetchall()
        self.assertEqual(len(result), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'Not db storage')
    def test_all_cities(self):
        """Testign all from cities"""
        self.query.execute("SELECT * FROM cities")
        result = self.query.fetchall()
        self.assertEqual(len(result), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'Not db storage')
    def test_add(self):
        """Testing all from states"""
        self.query.execute("SELECT * FROM states")
        query_rows = self.query.fetchall()
        self.assertEqual(len(query_rows), 0)
        state = State(name="SomeName")
        state.save()
        self.db.autocommit(True)
        self.query.execute("SELECT * FROM states")
        query_rows = self.query.fetchall()
        self.assertEqual(len(query_rows), 1)


if __name__ == "__main__":
    unittest.main()
