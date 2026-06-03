# Title: Object-Oriented Vehicle Rental Engine
# Objective: To master Python OOP fundamentals including inheritance, polymorphism, encapsulation, and abstraction through a practical vehicle-renting simulation.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id: str, brand: str, model: str, base_rate: float):
        self._vehicle_id = vehicle_id
        self._brand = brand
        self._model = model
        self._base_rate = base_rate
        self._is_rented = False

    @property
    def vehicle_id(self) -> str:
        return self._vehicle_id

    @property
    def is_rented(self) -> bool:
        return self._is_rented

    @abstractmethod
    def calculate_cost(self, days: int) -> float:
        pass

    def rent(self) -> bool:
        if not self._is_rented:
            self._is_rented = True
            return True
        return False

    def return_vehicle(self) -> None:
        self._is_rented = False

    def __str__(self) -> str:
        status = "Unavailable" if self._is_rented else "Available"
        return f"{self._brand} {self._model} ({status})"

class Car(Vehicle):
    def __init__(self, vehicle_id: str, brand: str, model: str, base_rate: float, luxury_tier: bool):
        super().__init__(vehicle_id, brand, model, base_rate)
        self._luxury_tier = luxury_tier

    def calculate_cost(self, days: int) -> float:
        multiplier = 1.5 if self._luxury_tier else 1.0
        return self._base_rate * days * multiplier

class Motorcycle(Vehicle):
    def __init__(self, vehicle_id: str, brand: str, model: str, base_rate: float, engine_size: int):
        super().__init__(vehicle_id, brand, model, base_rate)
        self._engine_size = engine_size

    def calculate_cost(self, days: int) -> float:
        fee = 15.0 if self._engine_size > 500 else 0.0
        return (self._base_rate + fee) * days

    def __str__(self) -> str:
        return f"{super().__str__()} - {self._engine_size}cc"

class RentalManager:
    def __init__(self):
        self._vehicles = {}

    def add_vehicle(self, vehicle: Vehicle) -> None:
        self._vehicles[vehicle.vehicle_id] = vehicle

    def get_available(self) -> list:
        return [v for v in self._vehicles.values() if not v.is_rented]

    def execute_rental(self, vehicle_id: str, days: int) -> float:
        vehicle = self._vehicles.get(vehicle_id)
        if vehicle and vehicle.rent():
            return vehicle.calculate_cost(days)
        return -1.0

    def execute_return(self, vehicle_id: str) -> bool:
        vehicle = self._vehicles.get(vehicle_id)
        if vehicle and vehicle.is_rented:
            vehicle.return_vehicle()
            return True
        return False

if __name__ == "__main__":
    manager = RentalManager()
    manager.add_vehicle(Car("C101", "Tesla", "Model S", 100.0, True))
    manager.add_vehicle(Car("C102", "Toyota", "Corolla", 40.0, False))
    manager.add_vehicle(Motorcycle("M201", "Yamaha", "R1", 50.0, 998))
    manager.add_vehicle(Motorcycle("M202", "Honda", "Super Cub", 20.0, 110))

    for v in manager.get_available():
        print(f"ID: {v.vehicle_id} | {v}")

    cost_tesla = manager.execute_rental("C101", 3)
    cost_honda = manager.execute_rental("M202", 3)

    print(f"Rented C101 for 3 days. Cost: ${cost_tesla:.2f}")
    print(f"Rented M202 for 3 days. Cost: ${cost_honda:.2f}")

    print("\nAvailable vehicles after rentals:")
    for v in manager.get_available():
        print(f"ID: {v.vehicle_id} | {v}")

    manager.execute_return("C101")