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
