

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
