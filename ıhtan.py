stats = {
    "Strength": 1,
    "Armor": 1,
    "Outdoormanship": 1,
    "Craftmanship": 1,
    "Love": 1,
    "Friendship": 1
}

Inventory = {
    "Wood": 1,
    "Stone": 1,
    "Flint": 1,
    "Water(L)": 2,
    "Food": 1
}

def show_inventory():
    print("\n=== Inventory ===")
    for item, amount in Inventory.items():
        print(f"{item}: {amount}") 

def show_stats():
    print("\n=== Stats ===")
    for stat, value in stats.items():
        print(f"{stat}: {value}")

def chopwood():
    print("You chopped down some wood. +5 wood added to your inventory")
    Inventory["Wood"] += 5

def foragefood():
    print("You foraged some food. +5 food added to your inventory")
    Inventory["Food"] += 5
    stats["Outdoormanship"] += 1

def minestones():
    print("You mined some stones. +5 stones added to your inventory.")
    Inventory["Stone"] += 5

def collectwater():
    print("You collected water from the stream. +5 water added to your inventory.")
    Inventory["Water(L)"] += 5

def char_creation():
    print("Welcome, young and courageous warrior. Your adventure begins here. Type in your name to go on with your journey.")
    name = input()
    print(f"It is so nice to meet you, {name}. Please choose your gender (boy/girl).")
    gender = input()
    if gender == "boy":
        print("Choose your dress: 1:Braies 2:Hose 3:Doublet 4:Houppelande")
        dress = input()
        print(f"Wise choice with your {dress}. Go on out there and show the world what you got.")
    elif gender == "girl":
        print("Choose your dress: 1:Kirtle 2:Cotehardie 3:Surcote 4:Mantle")
        dress2 = input()
        print(f"Wise choice with your {dress2}. Go on out there and show the world what you got.")

def startadventure():
    print("Loading...\nPlease type 'goo' to continue.")
    go = input()
    if go == "goo":
        print("Your adventure begins in an enormous forest full of trees.\nType 'inv' to see your inventory")
        inv = input()
        if inv == "inv":
            show_inventory()
            print("Type 'fire' to light up a fire.")
            fire = input()
            if fire == "fire":
                print("You lit up a smoldering fire. -1 Wood, +1 Craftmanship")
                Inventory["Wood"] -= 1
                stats["Craftmanship"] += 1
                print("You are getting hungry. Type 'food' to forage food.")
                food = input()
                if food == "food":
                    foragefood()

def game_loop():
    while True:
        print("\nWhat would you like to do?")
        print("1: Inventory | 2: Stats | 3: Chop Wood | 4: Forage Food | 5: Mine Stones | 6: Collect Water | q: Quit")
        choice = input()

        if choice == "1":
            show_inventory()
        elif choice == "2":
            show_stats()
        elif choice == "3":
            chopwood()
        elif choice == "4":
            foragefood()
        elif choice == "5":
            minestones()
        elif choice == "6":
            collectwater()
        elif choice == "q":
            print("Goodbye adventurer!")
            break

# Run game
char_creation()
startadventure()
game_loop()
