from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

from src.backend import crud, schemas
from src.backend.dependencies import get_db

router = APIRouter()
templates = Jinja2Templates(directory="C:\\Users\\ivanm\\PycharmProjects\\BookingSystem\\src\\Frontend")

@router.get("/")
def get_hotels(request: Request,db: Session = Depends(get_db)) -> _TemplateResponse:
    hotels = crud.get_hotels(db)
    return templates.TemplateResponse("pages/hotels.html", {"request": request, "hotels": hotels})
