from retailer_class import Retailer  # Assuming you have a Retailer class in a "retailer.py" file
from car_class import Car  # Assuming you have a Car class defined
import random
import datetime

class CarRetailer(Retailer):
    def __init__(self, retailer_id=0, retailer_name="Unknown Retailer", carretailer_address="Unknown Address",
                 carretailer_business_hours=(6.0, 18.0), carretailer_stock=None):
        super().__init__(retailer_id, retailer_name)
        self.carretailer_address = carretailer_address
        self.carretailer_business_hours = carretailer_business_hours
        self.carretailer_stock = carretailer_stock if carretailer_stock is not None else []

    def __str__(self):
        return f"{super().__str__()}, {self.carretailer_address}, {self.carretailer_business_hours}, {self.carretailer_stock}"

    def load_current_stock(self, path):
        with open(path, "r") as file:
            for line in file:
                car_code = line.strip()
                self.carretailer_stock.append(car_code)

    #def is_operating(self, cur_hour):
    #    start_hour, end_hour = self.carretailer_business_hours
    #    return start_hour <= cur_hour <= end_hour
    
    def is_operating():
        current_time = datetime.datetime.now().time()
        business_hours_start = datetime.time(9, 0)  # 9:00 AM
        business_hours_end = datetime.time(23, 0)   # 5:00 PM
        return business_hours_start <= current_time <= business_hours_end

    def get_all_stock(self):
         retailer_stock = [car for car in self.carretailer_stock if car["retailer_id"] == self.retailer_id]
         return retailer_stock

    def get_postcode_distance(self, postcode):
        retailer_postcode = int(self.carretailer_address.split()[-1])
        return abs(postcode - retailer_postcode)

    def remove_from_stock(self, car_code):
        if car_code in self.carretailer_stock:
            self.carretailer_stock.remove(car_code)
            return True
        else:
            return False

    def add_to_stock(self, car):
        if isinstance(car, Car):
            self.carretailer_stock.append(car.car_code)
            return True
        else:
            return False

    def get_stock_by_car_type(self, car_types):
        return [car for car in self.carretailer_stock if Car(car_code=car).get_car_type() in car_types]

    def get_stock_by_licence_type(self, licence_type):
        forbidden_types = ["P"] if licence_type == "L" else []
        return [car for car in self.carretailer_stock if not Car(car_code=car).probationary_licence_prohibited_vehicle() or Car(car_code=car).get_car_type() not in forbidden_types]

    def car_recommendation(self):
        if self.carretailer_stock:
            random_car_code = random.choice(self.carretailer_stock)
            return Car(car_code=random_car_code)
        else:
            return None

    def create_order(stock, retailer_id, car_id):
        print("Debug: Contents of stock list:")
        for car in stock:
            print(f"Car ID: {car['car_id']}, Retailer ID: {car['retailer_id']}")

        car = next((car for car in stock if car["retailer_id"] == retailer_id and car["car_id"] == car_id), None)

        if car is None:
            return "Car not found in stock."

        if not CarRetailer().is_operating():
            return "Sorry, the retailer is currently closed."

        order = f"Retailer ID: {retailer_id}, Car ID: {car_id}, Make: {car['make']}, Model: {car['model']}, Price: {car['price']}"

        with open("data/order.txt", "a") as file:
            file.write(order + "\n")

        return f"Order placed successfully:\n{order}"