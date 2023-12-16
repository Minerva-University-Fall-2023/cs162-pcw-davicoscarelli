class Animal:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def eat(self, food):
        print(f"{self.name} is eating {food}")

class Lion(Animal):
    def __init__(self, name, weight, age, mane_size):
        super().__init__(name, weight, age)
        self.mane_size = mane_size

    def roar(self):
        print(f"{self.name} is roaring")

class Giraffe(Animal):
    def __init__(self, name, weight, age, neck_length):
        super().__init__(name, weight, age)
        self.neck_length = neck_length

class Shark(Animal):
    def swim(self):
        print(f"{self.name} is swimming")

class Enclosure:
    def __init__(self, name, temperature_range, feeding_schedule):
        self.name = name
        self.temperature_range = temperature_range
        self.feeding_schedule = feeding_schedule
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

class Zoo:
    def __init__(self):
        self.enclosures = []

    def add_enclosure(self, enclosure):
        self.enclosures.append(enclosure)

zoo = Zoo()

savannah = Enclosure("Savannah", (25, 31), "Daily")
shark_tank = Enclosure("Shark Tank", (17, 18), "Weekly")

leo = Lion("Leo", 190, 5, "Large")
zara = Giraffe("Zara", 800, 7, "Long")
sammy = Shark("Sammy", 250, 3)

savannah.add_animal(leo)
savannah.add_animal(zara)
shark_tank.add_animal(sammy)

zoo.add_enclosure(savannah)
zoo.add_enclosure(shark_tank)

# Function to feed all animals in an enclosure
def feed_animals_in_enclosure(enclosure):
    for animal in enclosure.animals:
        if isinstance(animal, Lion):
            animal.eat("meat")
        elif isinstance(animal, Giraffe):
            animal.eat("leaves")
        elif isinstance(animal, Shark):
            animal.eat("fish")
        else:
            animal.eat("food")  # Generic food for animals not specifically handled

# Function to display information about an enclosure
def display_enclosure_info(enclosure):
    print(f"Enclosure: {enclosure.name}")
    print(f"Temperature Range: {enclosure.temperature_range}°C")
    print(f"Feeding Schedule: {enclosure.feeding_schedule}")
    print("Animals in Enclosure:")
    for animal in enclosure.animals:
        print(f" - {animal.name}, {animal.weight}kg, {animal.age} years old")

# Function to move an animal from one enclosure to another
def move_animal(animal, from_enclosure, to_enclosure):
    from_enclosure.remove_animal(animal)
    to_enclosure.add_animal(animal)
    print(f"Moved {animal.name} from {from_enclosure.name} to {to_enclosure.name}")

# Example interactions
print("Feeding animals in Savannah enclosure:")
feed_animals_in_enclosure(savannah)

print("\nFeeding animals in Shark Tank enclosure:")
feed_animals_in_enclosure(shark_tank)

print("\nDisplaying information about Savannah enclosure:")
display_enclosure_info(savannah)

print("\nDisplaying information about Shark Tank enclosure:")
display_enclosure_info(shark_tank)

# Moving an animal from one enclosure to another
print("\nMoving Sammy the Shark to Savannah enclosure:")
move_animal(sammy, shark_tank, savannah)

print("\nDisplaying updated information about Savannah enclosure:")
display_enclosure_info(savannah)

print("\nDisplaying updated information about Shark Tank enclosure:")
display_enclosure_info(shark_tank)


