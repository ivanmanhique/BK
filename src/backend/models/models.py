from datetime import datetime

from sqlalchemy import Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Destination(Base):
    __tablename__ = "destination"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    hotels = relationship("Hotel", back_populates="destination")


class Hotel(Base):
    __tablename__ = "hotel"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    destination_id = Column(Integer, ForeignKey("destination.id"))
    destination = relationship("Destination", back_populates="hotels")
    rooms = relationship("Room", back_populates="hotel")
    ratings = relationship("Rating", back_populates="hotel")


class Room(Base):
    __tablename__ = "room"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    hotel_id = Column(Integer, ForeignKey("hotel.id"))
    hotel = relationship("Hotel", back_populates="rooms")
    bookings = relationship("BookRoom", back_populates="room")


class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    date_of_birth = Column(Date)
    bookings = relationship("BookRoom", back_populates="client")
    ratings = relationship("Rating", back_populates="client")
    user = relationship("User", uselist=False, back_populates="client")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    password = Column(String)
    client_id = Column(Integer, ForeignKey("client.id"))
    client = relationship("Client", back_populates="user")


class Rating(Base):
    __tablename__ = "rating"

    id = Column(Integer, primary_key=True, autoincrement=True)
    rate = Column(Integer)
    client_id = Column(Integer, ForeignKey("client.id"))
    client = relationship("Client", back_populates="ratings")
    hotel_id = Column(Integer, ForeignKey("hotel.id"))
    hotel = relationship("Hotel", back_populates="ratings")


class BookRoom(Base):
    __tablename__ = "bookroom"

    id = Column(Integer, primary_key=True, autoincrement=True)
    start = Column(Date)
    end = Column(Date)
    client_id = Column(Integer, ForeignKey("client.id"))
    client = relationship("Client", back_populates="bookings")
    room_id = Column(Integer, ForeignKey("room.id"))
    room = relationship("Room", back_populates="bookings")


