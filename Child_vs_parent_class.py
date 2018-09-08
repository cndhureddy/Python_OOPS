#Overriding the Functionality of a Parent Class

class Dog:
    species = 'mammal'

class SomeBreed(Dog):
    pass

class SomeOtherBreed(Dog):
    species = 'reptile'

frank = SomeBreed()
frank.species
#output: 'mammal'
beans = SomeOtherBreed()
beans.species
# output: 'reptile'
