#!/usr/bin/python3
"""set up database for storage"""

import os
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
        obj_types = [State, City, User, Amenity, Place, Review]

        for obj in obj_types:
#            print(obj)
 #           print("CLASS: {}".format(cls))
            if cls is None or cls in obj_types:
                '''query all objects'''
                for instance in self.__session.query(cls).all():
#                    print("instance: {}".format(instance))
                    key = obj.__name__ + '.' + instance.id
#                    print(key)
                    obj_dict[key] = instance
#            print("AAAAAAAAHHHBFDGDFVWDFBRVVEWSCDSFVWTVR!!!!!!!!!!!!!!!!") 
#            print(obj_dict)
#            print("DICT WAS PRINTED""")
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

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
