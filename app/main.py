from typing import List


class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark >= self.clean_power:
            return 0
        cost = (
                car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
                / self.distance_from_city_center
        )
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> float:
        washing_cost = self.calculate_washing_price(car)
        if washing_cost > 0:
            car.clean_mark = self.clean_power
        return washing_cost

    def serve_cars(self, cars: List[Car]) -> float:
        income = sum(self.wash_single_car(car) for car in cars)
        return round(income, 1)

    def rate_service(self, rate: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += rate
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)


bmw = Car(comfort_class=3, clean_mark=3, brand="BMW")
audi = Car(comfort_class=4, clean_mark=9, brand="Audi")
wash_station = CarWashStation(distance_from_city_center=5, clean_power=6, average_rating=3.5, count_of_ratings=6)
total_income = wash_station.serve_cars([bmw, audi])
print(total_income)  # 22.4
print(bmw.clean_mark)  # 6
