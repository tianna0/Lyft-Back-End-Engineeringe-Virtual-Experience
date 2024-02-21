from datetime import date
from battery.nubbin_battery import NubbinBattery

def test_needs_service_true():
    current_date = date.fromisoformat("2020-05-15")
    last_service_date = date.fromisoformat("2016-01-25")
    battery = NubbinBattery(current_date, last_service_date)
    assert battery.needs_service() == True

def test_needs_service_false():
    current_date = date.fromisoformat("2020-05-15")
    last_service_date = date.fromisoformat("2019-01-10")
    battery = NubbinBattery(current_date, last_service_date)
    assert battery.needs_service() == False

