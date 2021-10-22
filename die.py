from random import randint

class Die:
    #Class of a Single Die

    def __init__(self, num_sides=6):
        #Assume a six sides die
        self.num_sides = num_sides

    def roll(self):
        #Return a random value between 1 and number of sides
        return randint(1,self.num_sides)
