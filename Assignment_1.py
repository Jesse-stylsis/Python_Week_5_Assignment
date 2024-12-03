# Smartphone class
class Smartphone:
    def __init__(self, brand, model, battery, storage):
        # Constructor to initialize object attributes
        self.brand = brand
        self.model = model
        self.battery = battery  # in percentage
        self.storage = storage  # in GB
    
    def call(self, phone_number):
        print(f"Calling {phone_number}...")
    
    def text(self, phone_number, message):
        print(f"Texting {phone_number}: {message}")
    
    def check_battery(self):
        print(f"Battery is at {self.battery}%")
    
    def check_storage(self):
        print(f"Storage is at {self.storage}GB")

# Create a smartphone object
phone = Smartphone("Apple", "iPhone 13", 85, 128)

# Use the methods
phone.call("123-456-7890")
phone.text("123-456-7890", "Hello!")
phone.check_battery()
phone.check_storage()
