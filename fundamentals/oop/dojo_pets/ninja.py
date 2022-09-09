class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

def walk(self):
    self.pet.play()
    return self

def feed(self):
    if len(self.pet_food) > 0:
        food = self.pet_food.pop()
        print(f"Feeding {self.pet.name} {food}!")
        self.pet.eat()
    else:
        print("Oh no!!! you need more pet food!")
    return self

def bathe(self):
    self.pet.noise()

class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

def sleep(self):
    self.energy += 25
    return self

def eat(self):
    self.energy += 5
    self.health += 10
    return self

def play(self):
    self.health += 5
    return self

def noise(self):
    print(self.noise)

my_treats = ['bacon', 'cheese', 'icecube']
my_pet_food = ['kibble', 'meat', 'lamb']

pompers = Pet("pompers", "poodle", ['fast runner', 'extreme cuteness'], "woof, woof")

mimi = Ninja("Michelle", "Pow", pompers, my_treats, my_pet_food)

mimi.feed().walk().bathe()
