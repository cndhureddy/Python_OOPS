#While instance attributes are specific to each object, class attributes are the same for all instances.
#So while each dog has a unique name and age, every dog will be a mammal.

class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
