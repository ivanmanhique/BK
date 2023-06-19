from dataclasses import dataclass
from typing import Callable, Iterable

from sqlalchemy import create_engine
from sqlalchemy.engine import Connection, Engine
from sqlalchemy.orm import Session, sessionmaker

DB_URL = "sqlite:///booking_system.db"


@dataclass
class DbState:
    engine: Engine
    connection: Connection
    get_db: Callable[[], Iterable[Session]]


def create_db_state() -> DbState:
    engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
    connection = engine.connect()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def get_db() -> Iterable[Session]:
        with SessionLocal() as db:
            yield db

    return DbState(engine=engine, connection=connection, get_db=get_db)


def close_db_state(db_state: DbState) -> None:
    db_state.connection.close()


db_state = create_db_state()
get_db = db_state.get_db