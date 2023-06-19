import datetime
from typing import List

from pydantic import BaseModel


# Client:
class ClientBase(BaseModel):
    firstname: str
    lastname: str
    dateOfBirth: datetime.date


class ClientCreate(ClientBase):
    pass


class Client(ClientBase):
    # id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    password: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    pass


# Destination:
class DestinationBase(BaseModel):
    name: str


class DestinationCreate(DestinationBase):
    pass


class Destination(DestinationBase):
    # id: int

    class Config:
        orm_mode = True


# Room:
class RoomBase(BaseModel):
    name: str
    price: int
    # bookings = list[BookRoom]


class RoomCreate(RoomBase):
    pass


class Room(RoomBase):
    # d: int

    class Config:
        orm_mode = True


# Hotel:
class HotelBase(BaseModel):
    name: str
    destination: Destination
    # ratings = list[Rating]


class HotelCreate(HotelBase):
    pass


class Hotel(HotelBase):
    # id: int

    class Config:
        orm_mode = True


# BookRoom:
class BookRoomBase(BaseModel):
    name: str
    start: datetime.date
    end: datetime.date
    client: Client
    room: Room


class BookRoomCreate(BookRoomBase):
    pass


class BookRoom(BookRoomBase):
    # id: int

    class Config:
        orm_mode = True
