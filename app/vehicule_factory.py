# app/vehicle_factory.py
from app.models import Vehicle


class VehicleFactory:
    @staticmethod
    def create_vehicle(type, license_plate, user_id):
        # For simplicity, we are not differentiating vehicle types
        return Vehicle(license_plate=license_plate, user_id=user_id)
