from typing import Optional


class Human:
    def __init__(self, name: str, cars: list[str]) -> None:
        self.name = name
        self.cars = cars
        self.current_car: Optional[str] = None

    def set_current_car(self, car: str) -> None:
        if car not in self.cars:
            raise ValueError("No such car found {car}")
        self.current_car = car

def choose_a_car(human: Human) -> None:
    selected_car = input(f"Please select a car from {human.cars}")
    try:
        human.set_current_car(selected_car)
    except ValueError:
        print("No such cars, try again!")
        choose_a_car(human)

human = Human("Michael", ["Tesla", "2HK6784LXG34H78R1", "Roadster)))"])
human2 = Human("Gordon", ["Porsche", "9K7395CC185I7G9NB", "Taycan)))"])
choose_a_car(human2)
choose_a_car(human)
print(human.current_car)