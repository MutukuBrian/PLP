# Parent 
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        return f"{self.brand} {self.model} is now ON."

# Child 
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model)
        self.storage = storage
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        return f"Captured a photo using {self.camera_megapixels}MP camera!"

    def get_specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Camera: {self.camera_megapixels}MP"

phone = Smartphone("Samsung", "Galaxy S22", 128, 50)
print(phone.power_on())
print(phone.take_photo())
print(phone.get_specs())