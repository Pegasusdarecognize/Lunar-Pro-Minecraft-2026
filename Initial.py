from dataclasses import dataclass
from datetime import datetime


@dataclass
class Appointment:
    title: str
    date: datetime
    duration: int


class Calendar:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, title, date, duration):
        appointment_date = datetime.strptime(date, "%Y-%m-%d %H:%M")
        self.appointments.append(
            Appointment(title, appointment_date, duration)
        )

    def sort_appointments(self):
        self.appointments.sort(key=lambda appointment: appointment.date)

    def get_total_duration(self):
        return sum(
            appointment.duration
            for appointment in self.appointments
        )

    def print_schedule(self):
        print("Calendar Schedule")
        print("=================")

        for appointment in self.appointments:
            formatted_date = appointment.date.strftime(
                "%Y-%m-%d %H:%M"
            )

            print(
                f"{formatted_date} | "
                f"{appointment.title} | "
                f"{appointment.duration} min"
            )

        print("=================")
        print(f"Appointments: {len(self.appointments)}")
        print(f"Total Duration: {self.get_total_duration()} min")


calendar = Calendar()

calendar.add_appointment(
    "Team Meeting",
    "2026-09-15 10:00",
    60
)

calendar.add_appointment(
    "Project Review",
    "2026-09-13 14:30",
    90
)

calendar.add_appointment(
    "Client Call",
    "2026-09-14 11:15",
    45
)

calendar.add_appointment(
    "Development Session",
    "2026-09-16 09:00",
    120
)

calendar.sort_appointments()
calendar.print_schedule()