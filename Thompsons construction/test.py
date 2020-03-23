# Aaron Moran
# Practice using classes in Python

class Dog:
    # Member variables
    name = None
    breed = None
    owner = None

    def __init__(self, name=None, breed=None, owner=None):
        self.name= name
        self.breed = breed
        self.owner = owner
    
    # Constructor to fill out details
    def createNewDog(self):
        self.name = input("name : ")
        self.breedbreed = input("age : ")
        self.owner = input("owner : ")

# Create a student object
newDog = Dog()
newDog.createNewDog()
print("----------------------------------------")
print("Your name is : ", newDog.name)
print("Your breed is : ", newDog.breed)
print("Your owner is : ", newDog.owner)
newDog = Dog(name='Milo', breed='Springer', owner='Blaine')
print(newDog)