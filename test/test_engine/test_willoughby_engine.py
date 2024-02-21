from engine.willoughby_engine import WilloughbyEngine

def test_needs_service_true():
    # Test case where the mileage difference is more than 60000, expecting service need
    engine = WilloughbyEngine(current_mileage=100000, last_service_mileage=39000)
    assert engine.needs_service() is True, "Engine should need service due to high mileage difference"

def test_needs_service_false():
    # Test case where the mileage difference is not more than 60000, expecting no service need
    engine = WilloughbyEngine(current_mileage=95000, last_service_mileage=35000)
    assert engine.needs_service() is False, "Engine should not need service as the mileage difference is within limits"
