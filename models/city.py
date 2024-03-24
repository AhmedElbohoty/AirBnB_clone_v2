#!/usr/bin/python3
'''
City
'''
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    '''City:

    Attributes:
        name (str): city.
        state_id (str): The State id.
    '''
    if models.is_db:
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', backref='cities')
    else:
        state_id = ''
        name = ''

    def __init__(self, *args, **kwargs):
        '''Init city'''
        super().__init__(*args, **kwargs)
