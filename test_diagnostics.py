import pytest
from diagnostics import read_dtc_codes, clear_dtc_codes, vehicle_speed_status

def test_read_dtc_codes():
    assert "P0130" in read_dtc_codes()
    
def test_clear_dtc_codes():
    assert clear_dtc_codes() is True

@pytest.mark.parametrize("speed, expected", [(0,"stationary"),(30,"moving")])

def test_vehicle_speed_status(speed,expected):
    assert vehicle_speed_status(speed) == expected
    
def test_vehicle_speed_negative():
    with pytest.raises(ValueError):
        vehicle_speed_status(-10)
