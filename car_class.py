class Car:
    def __init__(self, car_code="XX000000", car_name="Unknown", car_capacity=5, car_horsepower=100, car_weight=1500, car_type="FWD"):
        self.car_code = car_code
        self.car_name = car_name
        self.car_capacity = car_capacity
        self.car_horsepower = car_horsepower
        self.car_weight = car_weight
        self.car_type = car_type

    def __str__(self):
        return f"{self.car_code}, {self.car_name}, {self.car_capacity}, {self.car_horsepower}, {self.car_weight}, {self.car_type}"

    def probationary_licence_prohibited_vehicle(self):
        power_to_mass_ratio = (self.car_horsepower * 1000) / self.car_weight
        return power_to_mass_ratio > 130

    def found_matching_car(self, car_code_to_find):
        return self.car_code == car_code_to_find

    def get_car_type(self):
        return self.car_type
    
