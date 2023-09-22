import os
import random
import datetime
from car_retailer import CarRetailer

# Function to generate random test data and save it to "stock.txt"
def generate_test_data():
    car_retailers = [
        {"retailer_id": 1, "name": "ABC Cars", "postcode": "12345"},
        {"retailer_id": 2, "name": "XYZ Motors", "postcode": "54321"},
    ]

    car_types = ["AWD", "RWD", "FWD"]
    stock = []

    for retailer in car_retailers:
        for _ in range(random.randint(5, 10)):
            car = {
                "car_id": random.randint(100, 999),
                "make": random.choice(["Toyota", "Honda", "Ford", "Nissan"]),
                "model": random.choice(["Sedan", "SUV", "Truck"]),
                "car_type": random.choice(car_types),
                "price": random.randint(10000, 50000),
                "year": random.randint(2010, 2023),
                "retailer_id": retailer["retailer_id"],
            }
            stock.append(car)

    with open("data/stock.txt", "w") as file:
        for car in stock:
            file.write(
                f"{car['car_id']}|{car['make']}|{car['model']}|{car['car_type']}|{car['price']}|{car['year']}|{car['retailer_id']}\n"
            )

# Function to load stock data from "stock.txt"
def load_stock_data():
    stock = []
    with open("data/stock.txt", "r") as file:
        for line in file:
            car_data = line.strip().split("|")
            stock.append(
                {
                    "car_id": int(car_data[0]),
                    "make": car_data[1],
                    "model": car_data[2],
                    "car_type": car_data[3],
                    "price": int(car_data[4]),
                    "year": int(car_data[5]),
                    "retailer_id": int(car_data[6]),
                }
            )
    return stock

# Function to get the nearest car retailer based on user's postcode
def find_nearest_retailer(postcode):
    retailers = [
        {"retailer_id": 1, "name": "ABC Cars", "postcode": "12345"},
        {"retailer_id": 2, "name": "XYZ Motors", "postcode": "54321"},
    ]
    
    def calculate_distance(p1, p2):
        return abs(int(p1) - int(p2))
    
    nearest_retailer = min(
        retailers,
        key=lambda retailer: calculate_distance(retailer["postcode"], postcode),
    )
    
    return nearest_retailer

# Function to recommend a random car
def recommend_car(stock, retailer_id):
    retailer_stock = [car for car in stock if car["retailer_id"] == retailer_id]
    if retailer_stock:
        return random.choice(retailer_stock)
    else:
        return None

# Function to get all cars in stock for a retailer
#def get_all_cars_in_stock(stock, retailer_id):
#    retailer_stock = [car for car in stock if car["retailer_id"] == retailer_id]
#    return retailer_stock

# Function to get cars in stock by car types for a retailer
def get_cars_in_stock_by_type(stock, retailer_id, car_type):
    retailer_stock = [car for car in stock if car["retailer_id"] == retailer_id and car["car_type"] == car_type]
    return retailer_stock

# Function to check if the current time is within business hours
def is_business_hours():
    current_time = datetime.datetime.now().time()
    business_hours_start = datetime.time(9, 0)  # 9:00 AM
    business_hours_end = datetime.time(23, 0)   # 5:00 PM
    return business_hours_start <= current_time <= business_hours_end

#def place_car_order(stock, retailer_id, car_id):
#    print("Debug: Contents of stock list:")
#    for car in stock:
#        print(f"Car ID: {car['car_id']}, Retailer ID: {car['retailer_id']}")
#
#    car = next((car for car in stock if car["retailer_id"] == retailer_id and car["car_id"] == car_id), None)
#    
#    if car is None:
#        return "Car not found in stock."
#    
#    if not is_business_hours():
#        return "Sorry, the retailer is currently closed."
#
#    order = f"Retailer ID: {retailer_id}, Car ID: {car_id}, Make: {car['make']}, Model: {car['model']}, Price: {car['price']}"
#
#    with open("data/order.txt", "a") as file:
#        file.write(order + "\n")
#
#    return f"Order placed successfully:\n{order}"

# Main program loop
if __name__ == "__main__":
    if not os.path.exists("data"):
        os.mkdir("data")

    if not os.path.exists("data/stock.txt"):
        generate_test_data()

    stock = load_stock_data()
    car_retailers = [
        {"retailer_id": 1, "name": "ABC Cars"},  # Replace with your retailer data
        {"retailer_id": 2, "name": "XYZ Motors"},  # Replace with your retailer data
    ]

    while True:
        print("\nCar Purchase Advisor System")
        print("Options:")
        print("a) Look for the nearest car retailer")
        print("b) Get car purchase advice")
        print("c) Place a car order")
        print("d) Exit")

        choice = input("Enter your choice: ").lower()

        if choice == "a":
            postcode = input("Enter your postcode: ")
            nearest_retailer = find_nearest_retailer(postcode)
            print(f"The nearest car retailer is: {nearest_retailer['name']}")
        
        elif choice == "b":
            print("Available car retailers:")
            for retailer in car_retailers:
                print(f"Retailer ID: {retailer['retailer_id']}, Name: {retailer['name']}")
            
            retailer_id = int(input("Select a car retailer (Enter Retailer ID): "))
            current_retailer = None

            for retailer in car_retailers:
                if retailer["retailer_id"] == retailer_id:
                    current_retailer = CarRetailer(
                        retailer_id=retailer["retailer_id"],
                        retailer_name=retailer["name"],
                        carretailer_stock=stock  # Pass the loaded stock data
                    )
                    break
            
            if current_retailer is not None:
                print(f"Selected Car Retailer: {current_retailer.retailer_name}")
                print("Options:")
                print("i) Recommend a car")
                print("ii) Get all cars in stock")
                print("iii) Get cars in stock by car types")
                print("iv) Get probationary licence permitted cars in stock")

                sub_choice = input("Enter your choice (i/ii/iii/iv): ").lower()

                if sub_choice == "i":
                    recommended_car = current_retailer.car_recommendation()
                    if recommended_car:
                        print(f"Recommended Car: {recommended_car.car_name}")
                    else:
                        print("No cars available for recommendation.")

                elif sub_choice == "ii":
                    retailer_stock = current_retailer.get_all_stock()
                    if retailer_stock:
                        print("Cars in stock:")
                        for car in retailer_stock:
                            print(f"Car ID: {car['car_id']}, Make: {car['make']}, Model: {car['model']}")
                    else:
                        print("No cars available in stock.")

                elif sub_choice == "iii":
                    car_type = input("Enter car type (e.g., AWD, RWD, FWD): ")
                    retailer_stock = current_retailer.get_stock_by_car_type([car_type])
                    if retailer_stock:
                        print(f"Cars in stock with car type {car_type}:")
                        for car in retailer_stock:
                            print(f"Car ID: {car['car_id']}, Make: {car['make']}, Model: {car['model']}")
                    else:
                        print(f"No cars available with the specified car type ({car_type}).")

                elif sub_choice == "iv":
                    licence_type = input("Enter your licence type (L/P/Full): ")
                    if licence_type not in ["L", "P", "Full"]:
                        print("Invalid licence type. Please enter 'L', 'P', or 'Full'.")
                else:
                    retailer_stock = current_retailer.get_stock_by_licence_type(licence_type)
                    if retailer_stock:
                        print(f"Cars in stock permitted for {licence_type} licence:")
                        for car in retailer_stock:
                            print(f"Car ID: {car['car_id']}, Make: {car['make']}, Model: {car['model']}")
                    else:
                        print(f"No cars available for {licence_type} licence.")
                        
        elif choice == "c":
            retailer_id, car_id = map(int, input("Enter retailer ID and car ID (e.g., 1 123): ").split())
            result = CarRetailer.create_order(stock, retailer_id, car_id)
            print(result)
        
        elif choice == "d":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")
                    
                    