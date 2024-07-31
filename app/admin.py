# app/admin.py
from app.database import DatabaseAccess
from app.models import ParkingSlot, User, Report


class AdminService:
    def __init__(self):
        self.db = DatabaseAccess()

    def manage_parking_slot(self, location, is_available):
        session = self.db.get_session()
        slot = ParkingSlot(location=location, is_available=is_available)
        session.add(slot)
        session.commit()
        return slot

    def manage_user_account(self, username, password):
        session = self.db.get_session()
        user = User(username=username, password=password)
        session.add(user)
        session.commit()
        return user

    def generate_stats_report(self):
        session = self.db.get_session()
        # Example report generation logic
        report_content = "Report Content"
        report = Report(content=report_content)
        session.add(report)
        session.commit()
        return report
