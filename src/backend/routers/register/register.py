from datetime import datetime
from fastapi import Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException
from fastapi.openapi.models import Response
from fastapi.routing import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from src.backend import crud, schemas
from src.backend.dependencies import get_db
from src.backend.models import Client, Room, BookRoom, User

router = APIRouter()
templates = Jinja2Templates(directory="C:\\Users\\ivanm\\PycharmProjects\\BookingSystem\\src\\Frontend")


@router.get("/")
def register_page(request: Request):
    return templates.TemplateResponse("pages/signup.html", {"request": request})


@router.post("/")
async def register(request: Request, db: Session = Depends(get_db)):
    formData = await request.form()
    _email = formData.get("email")
    _password = formData.get("password")
    user = User(email=_email, password=_password)
    isAdded = crud.register(db, user)
    print(isAdded)
    if isAdded:
        return RedirectResponse("/login/")
    else:
        return RedirectResponse("/login/exists/")
