#!/usr/bin/python3
'''
BaseModel:
    is a class that defines all common attributes/methods for other classes.
'''

from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    '''Base class that defines all common attributes/methods for other classes

    Attributes:
        id (str): unique id.
        created_at (datetime): The datetime when an instance is created.
        updated_at (datetime): The datetime when an instance is created
                               and it will be updated with every changes.
    '''

    def __init__(self, *args, **kwargs):
        '''Initialize the instance

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        '''
        if not kwargs:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        '''Return the representation of Instance.'''
        instance_id = self.id
        classname = self.__class__.__name__
        instance_dict = self.__dict__
        return '[{}] ({}) {}'.format(classname, instance_id, instance_dict)

    def save(self):
        '''Updates the public instance attribute updated_at'''
        self.updated_at = datetime.now()

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

        return dictionary
