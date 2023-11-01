class DunderMania:
    '''This class is overloaded with dunder methods.'''

    def __init__(self, name="Unknown"):
        self.name = name

    def __str__(self):
        return f"This is the DunderMania class, and its name is {self.name}."

    def __len__(self):
        return len(self.name)

    def __bool__(self):
        return bool(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __add__(self, other):
        return DunderMania(self.name + other.name)


if __name__ == "__main__":
    obj1 = DunderMania("Lazy")
    obj2 = DunderMania("Me")
    obj3 = DunderMania("Lazy")  # Another object with the same name for equality testing

    # __str__ method
    print(obj1)  # Expected: This is the DunderMania class, and its name is Lazy.

    # __len__ method
    print(len(obj1))  # Expected: 4 (Length of the name "Lazy")

    # __add__ method
    combined_obj = obj1 + obj2
    print(combined_obj)  # Expected: This is the DunderMania class, and its name is LazyMe.

    # __bool__ method
    print(bool(obj1))  # Expected: True (Because the name is not empty)

    # __eq__ method
    print(obj1 == obj3)  # Expected: True (Because both have the name "Lazy")
    print(obj1 == obj2)  # Expected: False (Because their names are different)
