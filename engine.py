from abc import ABC, abstractmethod

from car import Car


class Engine(Car):
    @abstractmethod
    def needs_service() -> bool:
        pass


class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        if(self.current_mileage - self.last_service_mileage > 30000):
            return True
        else: 
            return False

class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        if(self.current_mileage - self.last_service_mileage > 60000):
            return True
        else:
            return False
        

class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool):
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        if(self.warning_light_on):
            return True
        else:
            return False