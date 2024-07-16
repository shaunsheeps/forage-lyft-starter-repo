from abc import ABC, abstractmethod


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Car(ABC):  
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        pass    