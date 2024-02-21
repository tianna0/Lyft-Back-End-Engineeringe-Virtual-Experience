from tires.octoprime_tires import OctoprimeTires

def test_needs_service_true():
    # Test case where the sum of tire wear levels equals or exceeds 3.0, expecting service need
    tire_wear_levels = [0.75, 0.75, 0.75, 0.75]  # Sum is 3.0
    tires = OctoprimeTires(tire_wear_levels)
    assert tires.needs_service() is True, "Tires should need service due to high total wear level"

def test_needs_service_true_with_higher_wear():
    # Additional test case where the sum of tire wear levels is greater than 3.0
    tire_wear_levels = [0.8, 0.8, 0.8, 0.8]  # Sum is 3.2
    tires = OctoprimeTires(tire_wear_levels)
    assert tires.needs_service() is True, "Tires should need service as total wear exceeds the threshold"

def test_needs_service_false():
    # Test case where the sum of tire wear levels is below 3.0, expecting no service need
    tire_wear_levels = [0.5, 0.5, 0.5, 0.5]  # Sum is 2.0
    tires = OctoprimeTires(tire_wear_levels)
    assert tires.needs_service() is False, "Tires should not need service as total wear level is below the threshold"
