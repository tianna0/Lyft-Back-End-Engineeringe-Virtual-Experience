from engine.sternman_engine import SternmanEngine

def test_needs_service_true():
    # Test case where the warning light is on
    engine = SternmanEngine(warning_light_is_on=True)
    assert engine.needs_service() == True, "Expected to need service when the warning light is on"

def test_needs_service_false():
    # Test case where the warning light is off
    engine = SternmanEngine(warning_light_is_on=False)
    assert engine.needs_service() == False, "Expected not to need service when the warning light is off"
