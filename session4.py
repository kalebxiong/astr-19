class FavoriteAnimal:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print("Physical Characteristics of My Favorite Animal:")
        print("Arm Length: {:.2f} meters".format(self.arm_length))
        print("Leg Length: {:.2f} meters".format(self.leg_length))
        print("Number of Eyes: {}".format(self.num_eyes))
        if self.has_tail:
            print("Has a Tail: Yes")
        else:
            print("Has a Tail: No")
        if self.is_furry:
            print("Is Furry: Yes")
        else:
            print("Is Furry: No")

# Create an instance of the FavoriteAnimal class
my_favorite_animal = FavoriteAnimal(1.2, 0.9, 2, True, True)

# Call the describe method to print the physical characteristics
my_favorite_animal.describe()