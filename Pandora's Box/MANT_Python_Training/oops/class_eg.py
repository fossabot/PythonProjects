class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_bird(self):
        print(self.age)
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
age=22
blu.print_bird()

Parrot.species = "animal"
print(Parrot.species)
# access the class attributes
#print("Blu is a {}".format(Parrot.species))
#print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
#print("{} is {} years old".format( blu.name, blu.age))
#print("{} is {} years old".format( woo.name, woo.age))
