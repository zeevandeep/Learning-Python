class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age
hippo=Animal("Cat",5)
Dog=Animal("Dog",7)
hippo.description()

hippo.is_alive = False
print hippo.is_alive
print Dog.is_alive