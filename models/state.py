#!/usr/bin/python
""" holds class State"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

class State(BaseModel, Base):
    """Representation of state """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", back_populates="state", cascade="all, delete, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """returns a list of City instances with state_id == current State.id"""
        all_instances = models.storage.all()
        query = []
        for key, value in all_instances.items():
            if key.startswith('City') and getattr(value, 'state_id') == self.id:
                query.append(value)
        return query
