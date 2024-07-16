from abc import ABC, abstractmethod
from datetime import date
from car import Car


class Battery:
    @abstractmethod
    def needs_service() -> bool:
        pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self) -> bool:
        service_threshold_date = self.current_date.year - self.last_service_date.year
        if(service_threshold_date >= 2):
            return True
        else:
            return False

class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = self.current_date.year - self.last_service_date.year
        if(service_threshold_date >= 4):
            return True
        else: 
            return False