from typing import Iterable

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql import Select

from src.backend import models
from src.backend.models import Hotel, Client, BookRoom
from src.backend.models.models import User, Destination, Room


def deleteBooking(db:Session, bookingId: int):
    booking = db.query(BookRoom).filter_by(id = bookingId).first()
    db.delete(booking)
    db.commit()


def getClientData(db: Session, user: User):
    client = db.query(Client).filter_by(email=user.email).first()
    result = db.query(BookRoom.id,Destination.name, Hotel.name, BookRoom.start, BookRoom.end). \
        join(Hotel).join(Room).join(BookRoom).join(Client). \
        filter(Client.email == user.email).all()
    return result, client.firstname


def register(db: Session, _user: User) -> bool:
    user = db.query(User).filter_by(email=_user.email).first()
    users = db.query(User).all()
    # Iterate over the users
    for __user in users:
        print("User pass:", __user.password)
        print("Email:", __user.email)

    if user is None:
        db.add(_user)
        db.commit()
        return True
    else:
        return False


def authenticate_user(db: Session, _email: str, _password: str) -> User:
    user = db.query(User).filter_by(email=_email, password=_password).first()
    users = db.query(User).all()
    # Iterate over the users
    for _user in users:
        print("User pass:", _user.password)
        print("Email:", _user.email)

    if user:
        return user
    else:
        return None


def createBooking(booking: BookRoom, db: Session):

    db.add(booking)
    db.commit()


def isUser(user: Client, db: Session):
    user_ = is_User_query(user, db)
    if user_ is None:
        try:
            db.add(user)
            db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            print("Error occurred during insertion:", str(e))
        finally:
            db.close()
    else:
        return user_
    return user


def is_User_query(user: Client, db: Session):
    query = db.query(models.Client).filter(models.Client.firstname == user.firstname).first()
    return query


def isHotel_Destination(hotel: str, destination: str, db: Session) -> bool:
    hotels = get_hotels_with_specific_destination(db, hotel)
    for hotel in hotels:
        if hotel.destination.name == destination:
            return True
    return False


def getHotel_Destination(db: Session, hotelName: str) -> models.Hotel:
    return db.query(models.Hotel).options(joinedload(models.Hotel.destination))\
        .filter(models.Hotel.name == hotelName).first()


def get_hotels_with_specific_destination(db: Session, hotelName: str) -> list[models.Hotel]:
    return db.query(models.Hotel).options(joinedload(models.Hotel.destination))\
        .filter(models.Hotel.name == hotelName).all()


def get_hotels_with_specific_destination_query(hotelName: str) -> Select[Iterable[models.Hotel]]:
    return select(models.Hotel).options(joinedload(Hotel.destination)).where(Hotel.name == hotelName)


def get_destinations(db: Session) -> list[models.Destination]:
    return list(db.scalars(get_destination_query()))


def get_destination_query() -> Select[Iterable[models.Destination]]:
    return select(models.Destination)


def get_hotels(db: Session) -> list[models.Hotel]:
    return list(db.scalars(get_hotel_query()))


def get_hotel_query() -> Select[Iterable[models.Hotel]]:
    return select(models.Hotel)


def get_rooms(db: Session) -> list[models.Room]:
    return list(db.scalars(get_room_query()))


def get_room_query() -> Select[Iterable[models.Room]]:
    return select(models.Room)


def book_room(db: Session):
    pass


def book_room_query():
    pass
