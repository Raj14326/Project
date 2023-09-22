import random

class Retailer:
    def __init__(self, retailer_id=0, retailer_name="Unknown Retailer"):
        self.retailer_id = retailer_id
        self.retailer_name = retailer_name

    def __str__(self):
        return f"{self.retailer_id}, {self.retailer_name}"  

    def generate_retailer_id(self, list_retailer):
        while True:
            new_id = random.randint(10000000, 99999999)  # Generate an 8-digit random ID
            if new_id not in [retailer.retailer_id for retailer in list_retailer]:
                self.retailer_id = new_id
                break
            
            # Create a list of existing retailers
existing_retailers = []

# Create a Retailer object
new_retailer = Retailer()
new_retailer.generate_retailer_id(existing_retailers)
new_retailer.retailer_name = "ABC Cars"
new=new_retailer
# Example usage of class methods
print(new_retailer)
existing_retailers.append(new)
print(str(existing_retailers))
