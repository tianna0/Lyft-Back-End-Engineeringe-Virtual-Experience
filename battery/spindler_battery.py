from battery.battery import Battery
from utils import add_years_to_date

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        battery_should_be_serviced = add_years_to_date(self.last_service_date, 3)
        if battery_should_be_serviced < self.current_date:
            return True
        else:
            return False
