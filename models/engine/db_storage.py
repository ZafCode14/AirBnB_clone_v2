#!/usr/bin/python3
"""Module with the DBStorage"""
import sqlalchemy
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Class with the sqldatabase"""
    __engine = None
    __session = None

    def __init__(self):
        """Inintializing database"""
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")
                    ), pool_pre_ping=True)

        if (getenv("HBNB_ENV") == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query objects from the current database session"""

        class_list = [State, City, User, Place, Review, Amenity]

        result = {}
        if cls is not None:
            if cls in class_list:
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    result[key] = obj
        else:
            for class_name in class_list:
                query_result = self.__session.query(class_name).all()
                for obj in query_result:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    result[key] = obj

        return result

    def new(self, obj):
        """Add the object to the database"""
        self.__session.add(obj)

    def save(self):
        """Coomit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current databaes sesssion"""
        self.__sesssion.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Private session attribute"""
        self.__session.__class__.close(self.__session)
        self.reload()
