#!/usr/bin/python3
'''
User:
    - It is a class that defines all common attributes/methods for users.
    - It inherits from BaseModel
'''
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    '''User:
    - It is a class that defines all common attributes/methods for users.
    - It inherits from BaseModel

    Attributes:
        email (str): user's email.
        password (str): user's password.
        first_name (str): user's first name.
        last_name (str): user's last name.
    '''

    first_name = ''
    last_name = ''
    email = ''
    password = ''

    if models.is_db:
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")

    def __init__(self, *args, **kwargs):
        '''Init user'''
        super().__init__(*args, **kwargs)
