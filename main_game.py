from starter import *

directions = ['north', 'east', 'south', 'west']

stables = Room("Stables", "These are the stables. There is a key in the corner. The house is to your east.")
house = Room("House", "You are in a small house. The stables are to the west, and the shop is north.")
shop = Room("Shop", "You are in a shop. The cupboard has a tarnished old lock. The meadow is to the east, and the house is to the south.")
meadow = Room("Meadow", "You are in a beautiful meadow. There is a clearing with an X marked in the middle. The shop is to the west.")



stables.exits = {"east": house}
house.exits = {"west": stables, "north": shop}
meadow.exits = {"west": shop}
shop.exits = {"east": meadow, "south": house}

player = Player(stables,{})
Key = Item("key", "It is a shiny bronze key.",False)
Shovel = Item("shovel", "It is a big silver shovel with a handle made of wood and designs etched upon it.",True)
Treasure_Chest = Item("treasure chest", "It was an enormous wooden chest with jewels the top and a tarnished gold lock.",True)

stables.items = {"key"}
meadow.items = {"Treasure_Chest"}
shop.items = {"shovel"}


stables.describe()
      
while True:
    answer = input("What do you want to do?")
    if (answer in directions):
        if answer in player.location.exits:
            player.location = player.location.exits[answer]
            player.location.describe()
        else:
            print("You can't go {} from here.".format(answer))
    elif answer == "inventory":
        for item in player.inventory:
            print(item) 
    elif answer == "use":
        answer = input("Which item would you like to use?")
        if answer in player.inventory:
            if answer == "key" and player.location == "shop":
                shovel = False
            if answer == "shovel" and player.location == "meadow":
                Treasure_Chest == False
                print("You won the game! Congratulations!")
                break 
                
    elif answer == "location":
        print (self.location)
                
    elif answer == "drop":
        answer = input("Which item do you want to drop?")
        if answer in player.inventory:
            player.location.item["key"] = Key
            del player.inventory["key"]
        if answer in player.inventory:
            player.location.item["shovel"] = Shovel
            del player.inventory["shovel"]

          
        
        
    
    
    elif answer == "help":
        print ("You must win the game by finding the treasure chest, which is hidden in one of these four places: the stables, the house, the shop, or the meadow.")
        print ("You will find other items that will help you find the treasure chest along the way.")
        print ("Enter which direction you want to go to get to a different place: north, south, east, or west. You will know where you can go from the place you are.")
        print ("Type inventory to know which items you have in your storage.")
        print ("Type use if you want to use an item in your inventory")
        print ("Type location to find the description of where you are.")
        print ("Type drop if you want to leave n item in your inventory in your current room.")
        
        
        


                
        