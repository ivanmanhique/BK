from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Destination, Hotel, Room, Client, Rating, BookRoom

DB_URL = "sqlite:///booking_system.db"
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)


#Base.metadata.create_all(engine)

# Create a session
session = Session()


# Seed your database with sample data
def seed_database():
    # Create destinations
    paris = Destination(name="Paris")
    rome = Destination(name="Rome")
    london = Destination(name="London")

    # Create hotels
    hotel1 = Hotel(name="Hotel A", destination=paris)
    hotel2 = Hotel(name="Hotel B", destination=rome)
    hotel3 = Hotel(name="Hotel C", destination=london)

    # Create rooms
    room1 = Room(name="Room 1", price=100, hotel=hotel1)
    room2 = Room(name="Room 2", price=150, hotel=hotel2)
    room3 = Room(name="Room 3", price=200, hotel=hotel3)

    # Create clients
    client1 = Client(firstname="John", lastname="Doe", email="john.doe@example.com", date_of_birth=datetime(1990, 1, 1))
    client2 = Client(firstname="Jane", lastname="Smith", email="jane.smith@example.com",
                     date_of_birth=datetime(1995, 5, 5))

    # Create bookings
    booking1 = BookRoom(start=datetime(2023, 6, 1), end=datetime(2023, 6, 7), client=client1, room=room1)
    booking2 = BookRoom(start=datetime(2023, 6, 10), end=datetime(2023, 6, 15), client=client2, room=room2)

    # Create ratings
    rating1 = Rating(rate=4, client=client1, hotel=hotel1)
    rating2 = Rating(rate=5, client=client2, hotel=hotel2)

    # Add objects to the session
    session.add_all(
        [paris, rome, london, hotel1, hotel2, hotel3, room1, room2, room3, client1, client2, booking1, booking2,
         rating1, rating2])

    # Commit the session to persist the data
    session.commit()


# Call the seed_database function to populate your database
seed_database()
