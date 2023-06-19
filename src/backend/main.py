from fastapi import FastAPI
import uvicorn

from dependencies import close_db_state, db_state
from models import Base
from routers import destinations as destinations_router
from routers import hotels as hotels_router
from routers import login as login_router
from routers import home as home_router
from routers import bookRooms as booking_router
from routers import register as register_router


app = FastAPI(
    on_startup=[lambda: Base.metadata.create_all(bind=db_state.engine)],
    on_shutdown=[lambda: close_db_state(db_state)],
)
app.include_router(router=destinations_router.router, prefix="/destinations")
app.include_router(router=hotels_router.router, prefix="/hotels")
app.include_router(router=login_router.router, prefix="/login")
app.include_router(router=home_router.router, prefix="/home")
app.include_router(router=booking_router.router, prefix="/booking")
app.include_router(router=register_router.router, prefix="/register")

app.mount('/static', home_router.router)
app.mount('/pages', home_router.router)
app.mount('/styles', home_router.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
