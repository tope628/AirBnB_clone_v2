#!/usr/bin/python3
""" holds class State"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import models


class State(BaseModel, Base):
    """Representation of state """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """returns a list of City instances with state_id = current State.id"""
        all_instances = models.storage.all(City)
        query = []
        for key, value in all_instances.items():
            if getattr(value, 'state_id') == self.id:
                query.append(value)
        return query
