from tires_service.tire import Tire


class CarriganTires(Tire):
    def __init__(self, tire_needs_change):
        self.tire_needs_change = tire_needs_change

    def needs_service(self):
        for tire in self.tire_needs_change:
            if tire >= 0.9:
                return True
        return False