# Who needs animals when you can have drinks?
class Beverage:
    def drink(self):
        return "Glug glug"

    def spill(self):
        return "Oops! Classic me."

class Alcoholic(Beverage):
    def drink(self):
        return "Cheers to the weekend... or Tuesday. Whatever."

class NonAlcoholic(Beverage):
    def drink(self):
        return "Refreshing and sober!"

class Beer(Alcoholic):
    def spill(self):
        return "Not my beer!"

class Wine(Alcoholic):
    pass  # Too classy to override anything

class Juice(NonAlcoholic):
    pass  # Just juice, nothing to see here

class Soda(NonAlcoholic):
    def drink(self):
        return "Ahh, the sweet taste of cavities."


if __name__ == "__main__":
    beer = Beer()
    print(beer.drink())
    print(beer.spill())