class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return "Animal sound"

class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def give_birth(self):
        return f"{self.name} the {self.species} has given birth"
    
    def speak(self):
        return "Mammal sound"

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan 

    def speak(self):
        return "Chirp"   

class Reptile(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def bask_in_sun(self):
        return f"{self.name} the {self.species} is basking in the sun"
    
    def speak(self):
        return "Hiss"

class Primate(Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def climb_trees(self):
        return f"{self.name} the {self.species} is climbing trees"
    
    def speak(self):
        return "Ooh ooh ah ah"

class Marsupial(Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def carry_baby(self):
        return f"{self.name} the {self.species} is carrying its baby"
    
    def speak(self):
        return "Marsupial sound"

class Aviary:
    def __init__(self):
        self.birds = []

    def add_bird(self, name, species):
        self.birds.append(Bird(name, species))

class ReptileEnclosure:
    def __init__(self):
        self.reptiles = []

    def add_reptile(self, name, species):
        self.reptiles.append(Reptile(name, species))