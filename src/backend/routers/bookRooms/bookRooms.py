from datetime import datetime

from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from src.backend import crud, schemas
from src.backend.dependencies import get_db
from src.backend.models import Client, Room, BookRoom

router = APIRouter()
templates = Jinja2Templates(directory="C:\\Users\\ivanm\\PycharmProjects\\BookingSystem\\src\\Frontend")


@router.get("/")
def booking_page(request: Request, db: Session = Depends(get_db)):
    destinations = crud.get_destinations(db)
    hotels = crud.get_hotels(db)
    return templates.TemplateResponse("pages/booking.html", {"request": request, "destinations": destinations,
                                                             "hotels": hotels})


@router.post("/")
async def book(request: Request, db: Session = Depends(get_db)):
    formData = await request.form()
    destination = formData.get("destination")
    hotel = formData.get("hotel")
    startDate = splitDate(formData.get("startDate"))
    endDate = splitDate(formData.get("endDate"))
    firstname = formData.get("firstname")
    lastname = formData.get("lastname")
    _email = formData.get("email")
    birthdate = splitDate(formData.get("birthdate"))

    booked = crud.isHotel_Destination(hotel, destination, db)
    if booked:
        _client = Client(firstname=firstname, lastname=lastname, email=_email, date_of_birth=birthdate)
        _user = crud.isUser(_client, db)
        _hotel = crud.getHotel_Destination(db, hotel)
        _destination = _hotel.destination
        _room = Room(hotel=_hotel)
        booking = BookRoom(start=startDate, end=endDate, client=_client, room=_room)

        crud.createBooking(booking, db)
        return templates.TemplateResponse("pages/bookingSuccessful.html", {"request": request})

    destinations = crud.get_destinations(db)
    hotels = crud.get_hotels(db)
    return templates.TemplateResponse("pages/bookingFailed.html", {"request": request, "destinations": destinations,
                                                                   "hotels": hotels})


@router.delete("/")
def delete_booking(request: Request, db: Session = Depends(get_db)):
    pass


def splitDate(date: str):
    day = int(date.split('/')[1])
    month = int(date.split('/')[0])
    year = int(date.split('/')[2])

    return datetime(year, month, day)
