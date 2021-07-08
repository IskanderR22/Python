


from classes.pirate import Pokemon # Grabbing from the classes folder, selecting the pirate file and importing the Pokemon class
                                    # So that we may inherit the class attribute and methods 
import math # Importing math functionality, like math.floor or math.ceil to round up or down a result 

# Type weaknesses 
# Fire beats grass
# Grass beats water
# Water beats fire
# Electric beats water
class Pikachu(Pokemon):

    def __init__( self , name ):
        super().__init__(self)
        self.name = name
        self.strength = 20
        self.speed = 25
        self.health = 80
        self.type = "electric"
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n Type:{self.type}")
        return self

    def attack( self , pokemon ):
        # pokemon.health -= self.strength + self.speed
        if pokemon.type == "water":
            pokemon.health -= math.ceil((self.strength + self.speed) * 1.5) # Does 62.5 damage, rounding down the result
        else:
            pokemon.health -= (self.strength + self.speed)
        return self

        
class Squirtle(Pokemon):
    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self.strength = 40
        self.speed = 12
        self.health = 150
        self.type = "water"


    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n Type:{self.type}")
        return self


    def attack( self , pokemon ):
        if pokemon.type == "fire":
            pokemon.health -= math.ceil((self.strength) * 1.5) # Does 62.5 damage, rounding down the result
        else:
            pokemon.health -= self.strength
        return self


class Charmander(Pokemon):
    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self.strength = 60
        self.speed = 40
        self.health = 100
        self.type = "fire"


    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n Type:{self.type}")
        return self


    def attack( self , pokemon ):
        if pokemon.type == "grass":
            pokemon.health -= math.ceil((self.strength) * 1.5)
        else:
            pokemon.health -= self.strength
        return self

