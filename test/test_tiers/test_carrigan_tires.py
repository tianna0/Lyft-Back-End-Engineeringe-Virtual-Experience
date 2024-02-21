from tires.carrigan_tires import CarriganTires

def test_needs_service_true():
    # Test case where at least one tire's wear level is 0.9 or more, expecting service need
    tire_wear_levels = [0.6, 0.7, 0.8, 0.9]
    tires = CarriganTires(tire_wear_levels)
    assert tires.needs_service() is True, "Tires should need service due to high wear on at least one tire"

def test_needs_service_true_with_higher_wear():
    # Additional test case where a tire's wear level exceeds 0.9
    tire_wear_levels = [0.4, 0.5, 0.6, 0.95]
    tires = CarriganTires(tire_wear_levels)
    assert tires.needs_service() is True, "Tires should need service as one exceeds the wear threshold"

def test_needs_service_false():
    # Test case where all tire's wear levels are below 0.9, expecting no service need
    tire_wear_levels = [0.1, 0.2, 0.3, 0.4]
    tires = CarriganTires(tire_wear_levels)
    assert tires.needs_service() is False, "Tires should not need service as all wear levels are below the threshold"
