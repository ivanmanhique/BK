from datetime import datetime
from pathlib import Path

from fastapi import Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException
from fastapi.openapi.models import Response
from fastapi.routing import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from src.backend import crud, schemas
from src.backend.dependencies import get_db
from src.backend.models import Client, Room, BookRoom, User

router = APIRouter()
current_dir = Path(__file__).resolve().parent.parent.parent.parent
templates = Jinja2Templates(directory=current_dir / "Frontend")


@router.get("/")
def login_page(request: Request):
    return templates.TemplateResponse("pages/login.html", {"request": request})


@router.post("/exists")
def login_page(request: Request):
    return templates.TemplateResponse("pages/loginExists.html", {"request": request})


@router.post("/")
async def login(request: Request, db: Session = Depends(get_db)):
    formData = await request.form()
    _email = formData.get("email")
    _password = formData.get("password")
    user = crud.authenticate_user(db, _email, _password)
    if user:
        print("logged")
        res, name = crud.getClientData(db, user)
        return templates.TemplateResponse("pages/userBookings.html", {"request": request, "res": res, "Name": name,
                                                                      "email": user.email})
    else:
        return templates.TemplateResponse("pages/login.html", {"request": request, "wrongPass": "Wrong Pass or email"})
