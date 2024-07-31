# main.py
from app.user import UserService
from app.admin import AdminService
from app.vehicule_factory import VehicleFactory
from app.database import DatabaseAccess, Base
from datetime import datetime


def main():
    # Initialize database
    db = DatabaseAccess()
    Base.metadata.create_all(db.engine)

    user_service = UserService()
    admin_service = AdminService()

    while True:
        print("\nSmart Parking System")
        print("1. Create User Account")
        print("2. Add Vehicle")
        print("3. Book Parking Slot")
        print("4. Make Payment")
        print("5. Admin: Manage Parking Slot")
        print("6. Admin: Generate Stats Report")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = user_service.create_account(username, password)
            print(f"User created: {user.username}")

        elif choice == "2":
            user_id = int(input("Enter user ID: "))
            license_plate = input("Enter license plate: ")
            vehicle = user_service.add_vehicle(user_id, license_plate)
            print(f"Vehicle added: {vehicle.license_plate}")

        elif choice == "3":
            user_id = int(input("Enter user ID: "))
            slot_id = int(input("Enter parking slot ID: "))
            start_time = input("Enter start time (YYYY-MM-DD HH:MM:SS): ")
            end_time = input("Enter end time (YYYY-MM-DD HH:MM:SS): ")
            start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
            booking = user_service.book_parking_slot(
                user_id, slot_id, start_time, end_time
            )
            print(f"Booking made: {booking.id}")

        elif choice == "4":
            booking_id = int(input("Enter booking ID: "))
            amount = float(input("Enter amount: "))
            payment = user_service.make_payment(booking_id, amount)
            print(f"Payment processed: {payment.amount}")

        elif choice == "5":
            location = input("Enter parking slot location: ")
            is_available = input("Is the slot available (yes/no): ").lower() == "yes"
            slot = admin_service.manage_parking_slot(location, is_available)
            print(f"Parking slot managed: {slot.location}")

        elif choice == "6":
            report = admin_service.generate_stats_report()
            print(f"Report generated: {report.content}")

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
