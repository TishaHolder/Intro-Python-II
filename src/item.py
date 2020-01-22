class Item:
    def __init__(self, name, description): #the name should be one word for ease in parsing later.
        self.name = name
        self.description = description    

    def __repr__(self):
        return self.name + ': ' + self.description

class Umbrella(Item):
    def __init__(self, name, description, size):
        super().__init__(name, description)
        self.size = size

    def __repr__(self):
        return super().__repr__() + ", size: " + self.size

class FlashLight(Item):
    def __init__(self, name, description, brightness):
        super().__init__(name, description)
        self.brightness = brightness

    def __repr__(self):
        return super().__repr__() + ", brightness:" + self.brightness

class Binoculars(Item):
    def __init__(self, name, description, magnification):
        super().__init__(name, description)
        self.magnification = magnification

    def __repr__(self):
        return super().__repr__() + ", magnification:" + self.magnification

class Directions(Item):
    def __init__(self, name, description, orientation):
        super().__init__(name, description)
        self.orientation = orientation

    def __repr__(self):
        return super().__repr__() + ", orientation:" + self.orientation

class Chest(Item):
    def __init__(self, name, description, status):
        super().__init__(name, description)
        self.status = status

    def __repr__(self):
        return super().__repr__() + ", status:" + self.status

class Food(Item):
    def __init__(self, name, description, quantity):
        super().__init__(name, description)
        self.quantity = quantity

    def __repr__(self):
        return super().__repr__() + ", quantity:" + str(self.quantity)

class Water(Item):
    def __init__(self, name, description, type):
        super().__init__(name, description)
        self.type = type

    def __repr__(self):
        return super().__repr__() + ", type:" + self.type


class Pillow(Item):
    def __init__(self, name, description, softness):
        super().__init__(name, description)
        self.softness = softness

    def __repr__(self):
        return super().__repr__() + ", softness:" + self.softness

class Sword(Item):
    def __init__(self, name, description, blade):
        super().__init__(name, description)
        self.blade = blade

    def __repr__(self):
        return super().__repr__() + ", blade:" + self.blade

