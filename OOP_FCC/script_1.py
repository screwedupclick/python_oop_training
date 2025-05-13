class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    def bark(self):
        print("Whoof Whoof")
        
        
class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number
        
        
owner1 = Owner("Arnaud", "666 rue des enfers", "666-666-666")   
dog1 = Dog("Bruce", "Scottish Terrier", owner1)
print(dog1.owner.name)

owner2 = Owner("DJ Nocide", "6 rue des enfers", "666-808-555")
dog2 = Dog("Freya", "Greyhound", owner2)
print(dog2.owner.name)
