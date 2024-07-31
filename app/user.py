# app/user.py
from app.database import DatabaseAccess
from app.models import User, Vehicle, Booking, Payment


class UserService:
    def __init__(self):
        self.db = DatabaseAccess()

    def create_account(self, username, password):
        session = self.db.get_session()
        user = User(username=username, password=password)
        session.add(user)
        session.commit()
        return user

    def add_vehicle(self, user_id, license_plate):
        session = self.db.get_session()
        vehicle = Vehicle(license_plate=license_plate, user_id=user_id)
        session.add(vehicle)
        session.commit()
        return vehicle

    def book_parking_slot(self, user_id, slot_id, start_time, end_time):
        session = self.db.get_session()
        booking = Booking(
            user_id=user_id, slot_id=slot_id, start_time=start_time, end_time=end_time
        )
        session.add(booking)
        session.commit()
        return booking

    def make_payment(self, booking_id, amount):
        session = self.db.get_session()
        payment = Payment(booking_id=booking_id, amount=amount)
        session.add(payment)
        session.commit()
        return payment
