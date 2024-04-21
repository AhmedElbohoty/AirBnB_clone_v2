#!/usr/bin/python3
'''
City
'''
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    '''City:

    Attributes:
        name (str): city.
        state_id (str): The State id.
    '''
    from models import is_db
    if is_db:
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities')
    else:
        state_id = ''
        name = ''

    def __init__(self, *args, **kwargs):
        '''Init city'''
        super().__init__(*args, **kwargs)
