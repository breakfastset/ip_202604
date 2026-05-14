import random

class Coin:
    """Define a class that models after 2 sided coin."""

    def __init__(self):  # self refers to current object.
        """Constructor to initialise attributes."""
        self.side_up = "Heads"   # only attribute
        # attribute describes characteristic of an object
        # a Person might have height, weight
        # a Flower might have colour, smell
        # all attributes must be defined in __init__

    def get_side_up(self):
        """Return the face of the coin."""
        return self.side_up

    def toss(self):
        """Toss the coin and update the side up."""
        value = random.randint(1,2)
        if value == 1:
            self.side_up = "Heads"
        else:
            self.side_up = "Tails"

    def __str__(self):
        """Return a string representation of the coin."""
        return f"My Coin: {self.side_up}"