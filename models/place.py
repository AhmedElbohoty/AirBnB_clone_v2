#!/usr/bin/python3
'''
State
'''
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base

if models.is_db:
    place_amenity = Table('place_amenity',
                          Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey(
                                     'places.id',
                              onupdate='CASCADE',
                              ondelete='CASCADE'),
                              primary_key=True),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey(
                                     'amenities.id',
                                     onupdate='CASCADE',
                                     ondelete='CASCADE'),
                                 primary_key=True))


class Place(BaseModel, Base):
    '''Represent a place.

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms.
        number_bathrooms (int): The number of bathrooms.
        max_guest (int): The maximum number of guests.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    '''

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    if models.is_db:
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 backref='place_amenities',
                                 viewonly=False)

    def __init__(self, *args, **kwargs):
        '''Init Place'''
        super().__init__(*args, **kwargs)

    if not models.is_db:
        @property
        def reviews(self):
            '''getter attribute returns Review'''
            from models.review import Review
            result = []

            revs = models.storage.all(Review)
            for review in revs.values():
                if review.place_id != self.id:
                    continue
                result.append(review)
            return result

        @property
        def amenities(self):
            '''getter attribute returns Amenity'''
            from models.amenity import Amenity
            res = []
            amenities = models.storage.all(Amenity)

            for amenity in amenities.values():
                if amenity.place_id != self.id:
                    return
                res.append(amenity)
            return res
