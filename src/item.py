class Item:
    def __init__(self, name, description): #the name should be one word for ease in parsing later.
        self.name = name
        self.description = description

    def __str__(self):
        return self.name + ': ' + self.description
