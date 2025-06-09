def read_dtc_codes():
    return ["P0130", "P0420", "U0121"]

def clear_dtc_codes():
    return True

def vehicle_speed_status(speed):
    if speed<0:
        raise ValueError("Invalid Speed")
    return "moving" if speed>0 else "stationary"