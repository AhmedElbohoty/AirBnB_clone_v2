#!/usr/bin/python3
'''
State
'''
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    '''State:

    Attributes:
        name (str): state.
    '''
    name = ''
    if models.is_db:
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')

    def __init__(self, *args, **kwargs):
        '''Init state'''
        super().__init__(*args, **kwargs)

    if not models.is_db:
        @property
        def cities(self):
            '''getter for list of city instances related to the state'''
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
