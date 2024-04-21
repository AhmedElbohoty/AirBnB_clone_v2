#!/usr/bin/python3
'''
State
'''
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    '''State:

    Attributes:
        name (str): state.
    '''
    from models import is_db
    if is_db:
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        '''Init state'''
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        '''Return the list of City objects from storage linked
        to the current State'''
        from models import storage
        from models.city import City

        city_list = []
        all_cities = storage.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
