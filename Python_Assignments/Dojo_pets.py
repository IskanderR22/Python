

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet):

        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet # We inserted the Pet class attributes and methods inside this variable
    
    def walk(self):
        self.pet.play() # We are accessing the method inside of Pet
        return self
    

    def feed(self):
        self.pet.eat() # We are accessing the method inside of Pet
        return self


    def bathe(self):
        self.pet.noise() # We are accessing the method inside of Pet
        return self


class Pet:
    def __init__(self, name, type, tricks):

        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.health = self.health + 25
        return self


    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 25
        print(f"Pet's health after it is fed: {self.health}")
        print(f"Pet's energy after it is fed: {self.energy}")
        return self


    def play(self):
        self.health = self.health + 5
        print(f"Pet's health after a walk: {self.health}")
        return self 


    def noise(self):
        print("Your pet says: Meow!")
        return self




ninja = Ninja("Iskander", "Rangel", "Cat nip", "Cat food", Pet("Zelda", "Cat", "Sit")) # We can use a object/class as a parameter for another class. 
                                                                                        # This will store all the attributes and methods from Pet in the pet parameter.
                                                                                        

ninja.feed().walk().bathe()
