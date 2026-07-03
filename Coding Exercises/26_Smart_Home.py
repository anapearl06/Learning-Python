# Smart Home Device Tracker

class SmartDevice:
    # Class attribute
    brand = "HomeTech"

    def __init__(self, device_name, power_status):
        self.device_name = device_name
        self.power_status = power_status

        # Shadow the class attribute
        self.brand = "CustomBrand"

    def get_status(self):
        status = "ON" if self.power_status else "OFF"
        return f"{self.device_name} is {status} - {self.brand}"


# Example
device1 = SmartDevice("AC", True)
device2 = SmartDevice("Fan", False)

print(device1.get_status())
print(device2.get_status())