from tires_service.tire import Tire


class OctoprimeTires(Tire):
    def __init__(self, tire_needs_change):
        self.tire_needs_change = tire_needs_change

    def needs_service(self):
        return sum(self.tire_needs_change) >= 3.0