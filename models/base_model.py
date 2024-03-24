#!/usr/bin/python3
'''
BaseModel:
    is a class that defines all common attributes/methods for other classes.
'''

from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
import models

if models.is_db:
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    '''Base class that defines all common attributes/methods for other classes

    Attributes:
        id (str): unique id.
        created_at (datetime): The datetime when an instance is created.
        updated_at (datetime): The datetime when an instance is created
                               and it will be updated with every changes.
    '''

    if models.is_db:
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.now)
        updated_at = Column(DateTime, default=datetime.now)

    def __init__(self, *args, **kwargs):
        '''Base class that defines all common attributes/methods for other classes

        Attributes:
            id (str): unique id.
            created_at (datetime): The datetime when an instance is created.
            updated_at (datetime): The datetime when an instance is created
                                and it will be updated with every changes.
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(
                    kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(
                    kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = datetime.now()

            print(kwargs.get("id", None))
            if kwargs.get("id", None) is None:
                self.id = str(uuid4())
            else:
                print("Not supposed to be here")
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        '''Return the representation of Instance.'''
        instance_id = self.id
        classname = self.__class__.__name__
        instance_dict = self.__dict__
        return '[{}] ({}) {}'.format(classname, instance_id, instance_dict)

    def save(self):
        '''Updates the public instance attribute updated_at'''
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''Returns a dictionary representation of a instance.

        Returns:
            dict: instance attributes.
        '''
        dictionary = {**self.__dict__}
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]

        return dictionary

    def delete(self):
        '''Delete storage'''
        models.storage.delete(self)
