from engine.capulet_engine import CapuletEngine

def test_needs_service_true():
    # Mileage difference is more than 30000
    engine = CapuletEngine(current_mileage=60000, last_service_mileage=29000)
    assert engine.needs_service() == True, "Expected to need service"

def test_needs_service_false():
    # Mileage difference is 30000 or less
    engine = CapuletEngine(current_mileage=50000, last_service_mileage=20000)
    assert engine.needs_service() == False, "Expected not to need service"
