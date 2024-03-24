#!/usr/bin/python3
'''
Review
'''

from sqlalchemy import Column, String, ForeignKey
import models
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    '''Review

    Attributes:
        text (str): review text.
        user_id (str): The User.id.
        place_id (str): The Place.id.
    '''

    if models.is_db:
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """Init Review"""
        super().__init__(*args, **kwargs)
