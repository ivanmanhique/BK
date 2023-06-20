from pathlib import Path

from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session


from src.backend import crud, schemas
from src.backend.dependencies import get_db

router = APIRouter()
current_dir = Path(__file__).resolve().parent.parent.parent.parent
templates = Jinja2Templates(directory=current_dir / "Frontend")

@router.get("/")
def get_destinations(request: Request, db: Session = Depends(get_db)):
    destinations = crud.get_destinations(db)
    return templates.TemplateResponse("pages/destinations.html", {"request": request, "destinations": destinations})
