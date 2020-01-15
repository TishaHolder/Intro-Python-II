class Item:
    def __init__(self, name, description): #the name should be one word for ease in parsing later.
        self.name = name
        self.description = description

    def __str__(self):
        return self.name + ': ' + self.description


class Umbrella(Item):
    def __init__(name, description, size):
        super().__init__(name, description)
        self.size = size

    def __str__(self):
        return self.name + ": " + self.description + ", rated: " + self.size

class Binoculars(Item):
    def __init__(name, description, magnification):
        super().__init__(name, description)
        self.magnification = magnification

    def __str__(self):
        return self.name + ": " + self.description + ", magnification:" + self.magnification

class TreasureChest(Item):
    def __init__(name, description, status):
        super().__init__(name, description)
        self.status = status

    def __str__(self):
        return self.name + ": " + self.description + ", status:" + self.status

class Axe(Item):
    def __init__(name, description, blade):
        super().__init__(name, description)
        self.blade = blade

    def __str__(self):
        return self.name + ": " + self.description + ", blade:" + self.blade

class FlashLight(Item):
    def __init__(name, description, brightness):
        super().__init__(name, description)
        self.brightness = brightness

    def __str__(self):
        return self.name + ": " + self.description + ", brightness:" + self.brightness