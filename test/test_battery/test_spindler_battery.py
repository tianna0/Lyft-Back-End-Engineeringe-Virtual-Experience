from datetime import date
from battery.spindler_battery import SpindlerBattery
from utils import add_years_to_date

def test_needs_service_true():
    # Scenario where the battery needs service
    current_date = date.fromisoformat("2023-01-01")
    last_service_date = date.fromisoformat("2019-01-01")  # More than 3 years ago
    battery = SpindlerBattery(current_date, last_service_date)
    assert battery.needs_service() == True, "Battery should need service but doesn't."

def test_needs_service_false():
    # Scenario where the battery does not need service
    current_date = date.fromisoformat("2021-01-01")
    last_service_date = date.fromisoformat("2019-12-31")  # Less than 3 years ago
    battery = SpindlerBattery(current_date, last_service_date)
    assert battery.needs_service() == False, "Battery should not need service but does."
