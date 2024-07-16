from abc import ABC
from car import Car
from datetime import date
from battery import *
from engine import *


class CarFactory:

    def create_calliope(current_date : date, last_service_date: date,
                        current_mileage : int, last_service_mileage: int) -> Car:
        engine = CapuletEngine
        battery = SpindlerBattery


    def create_glissade(current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine
        battery = SpindlerBattery

    def create_palindrome(current_date: date, last_service_date: date,
                          warning_light_on: bool) -> Car:
        engine = SternmanEngine
        battery = SpindlerBattery

    def create_rorschach(current_date: date, last_service_date: date,
                         current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine
        battery = NubbinBattery

    def create_thovex(current_date: date, last_service_date: date,
                      current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine
        battery = NubbinBattery