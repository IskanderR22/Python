
from ninja import Ninja
from pet import Pet 

new_ninja = Ninja("Iskander", "Rangel", "Cat nip", "Cat food", Pet("Zelda", "Cat", "Sit")) # We can use a object/class as a parameter for another class. 
                                                                                        # This will store all the attributes and methods from Pet in the pet parameter.


new_ninja.feed().walk().bathe()
