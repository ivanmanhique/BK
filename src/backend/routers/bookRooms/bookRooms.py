from datetime import datetime

from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from src.backend import crud, schemas
from pathlib import Path
from src.backend.dependencies import get_db
from src.backend.models import Client, Room, BookRoom, User

router = APIRouter()
current_dir = Path(__file__).resolve().parent.parent.parent.parent
templates = Jinja2Templates(directory=current_dir / "Frontend")


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
        # _user = crud.isUser(_client, db)
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


@router.post("/cancel/{booking_id}/{email}")
def delete_booking(request: Request, email: str,booking_id: int, db: Session = Depends(get_db)):
    crud.deleteBooking(db, booking_id)
    user = User(email=email)
    res, name = crud.getClientData(db, user)
    return templates.TemplateResponse("pages/userBookings.html", {"request": request, "res": res, "Name": name, "email": user.email})


def splitDate(date: str):
    day = int(date.split('/')[1])
    month = int(date.split('/')[0])
    year = int(date.split('/')[2])

    return datetime(year, month, day)
