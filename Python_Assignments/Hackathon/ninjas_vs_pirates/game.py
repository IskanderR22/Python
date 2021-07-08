

from classes.ninja import Pikachu  # Grabbing from the classes folder, selecting the ninja file and importing the Pikachu class
from classes.ninja import Squirtle # Grabbing from the classes folder, selecting the ninja file and importing the Squirtle class
from classes.ninja import Charmander # Grabbing from the classes folder, selecting the ninja file and importing the Charmander class

from classes.pirate import Pokemon # Grabbing from the classes folder, selecting the pirate file and importing the Pokemon class
import random


# trainer1 = input("What starter would you like to pick\n 1. Pikachu\m 2. Squirtle\n 3. Charmander")

# if trainer1 == 1:
#     poke1 = Pikachu("Mousy")
#     print(f"You chose: {poke1.name} the Pikachu")
#     random_battle = random.randint(2,3)
# if random_battle == 2:

# # elif trainer1 == 2:
#     poke2 = Squirtle("Donatelo")
# elif trainer1 == 3:
#     poke3 = Pokemon("Lizardon")


poke1 = Pikachu("Mousy")

poke2 = Squirtle("Donatelo")

poke3 = Charmander("Lizardon")

poke1.show_stats()

poke1.attack(poke2)
poke2.show_stats()

poke2.attack(poke3)
poke3.show_stats()

