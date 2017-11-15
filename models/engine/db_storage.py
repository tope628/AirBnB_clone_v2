#!/usr/bin/python
"""set up database for storage"""

import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

Base = declarative_base()

class DBStorage:
    """connect to MySQL database"""
    __engine = None
    __session = None
    user = os.getenv("HBNB_MYSQL_USER")
    passwd = os.getenv("HBNB_MYSQL_PWD")
    host = os.getenv("HBNB_MYSQL_HOST")
    db = os.getenv("HBNB_MYSQL_DB")

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                self.user, self.passwd, self.host, self.db))
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query objects of the specified class from the DB"""
        obj_dict = {}
        obj_types = [User, State, City, Amenity, Place, Review]

        if cls is None:
            '''query all objects'''
            for obj_type in obj_types:
                for instance in self.__session.query(obj_type):
                    key = obj_type.__name__ + '.' + instance.id
                    obj_dict[key] = instance
        else:
            for instance in self.__session.query(cls):
                key = cls.__name__ + '.' + instance.id
                obj_dict[key] = instance

        return obj_dict

    def new(self, obj):
        """add the object to the current DB session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current DB session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current DB session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
        else:
            pass

    def reload(self):
        """create all tables in the DB & the current session from the engine"""
        '''create_all creates tables if not already exist'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=some_engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
