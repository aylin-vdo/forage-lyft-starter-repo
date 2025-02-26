from battery.battery import Battery
from numpy import timedelta64 as np


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        battery_service_upcoming_date = self.last_service_date + np.timedelta64(3,'Y')
        if battery_service_upcoming_date < self.current_date:
            return True
        else:
            return False