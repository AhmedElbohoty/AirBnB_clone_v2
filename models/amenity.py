#!/usr/bin/python3
'''
Amenity
'''
from sqlalchemy import Column, String
import models
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    '''Amenity:

    Attributes:
        name (str): amenity.
    '''

    if models.is_db:
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        '''Init Amenity'''
        super().__init__(*args, **kwargs)
