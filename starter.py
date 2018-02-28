class Player:
    def __init__(self, location, inventory):
         self.location = location
         self.inventory = inventory
    def move(self, new_location):
        def look(self):
            pass
        def get_inventory(self):
            pass
        
class Room: 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exit = {} 
        self.items = {}
        
    def describe(self):
        print(self.description)
        
        
class Item:
    def __init__(self, name, description, hidden):
        self.name = name
        self.description = description
        self. hidden = hidden
    def use(self):
        pass