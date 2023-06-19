from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from starlette.templating import _TemplateResponse
from src.backend import crud
from src.backend.dependencies import get_db

router = APIRouter()
router.mount("/static",
             StaticFiles(directory="C:\\Users\\ivanm\\PycharmProjects\\BookingSystem\\src\\Frontend\\static"),
             name="static")
router.mount("/styles",
             StaticFiles(directory="C:\\Users\\ivanm\\PycharmProjects\\BookingSystem\\src\\Frontend\\styles"),
             name="styles")

templates = Jinja2Templates(directory="C:\\Users\\ivanm\\PycharmProjects\\BookingSystem\\src\\Frontend")


@router.get("/", response_class=HTMLResponse)
async def homepage(request: Request, db: Session = Depends(get_db)) -> _TemplateResponse:
    _destinations = crud.get_destinations(db)
    destinations = [_destination.name for _destination in _destinations]
    return templates.TemplateResponse("index.html", {"request": request, "tittle": "Booking.com",
                                                     "destinations": destinations})
