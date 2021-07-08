

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet):

        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        self.choose_pet = Pet()
    
    def walk(self):
        self.choose_pet.play()
        return self
    
    def feed(self):
        self.choose_pet.eat()
        return self

    def bathe(self):
        self.choose_pet.noise()
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
        return self

    def play(self):
        self.health = self.health + 5
        return self 

    def noise(self):
        print("Meow!")
        return self




ninja = Ninja()

pet = Pet()