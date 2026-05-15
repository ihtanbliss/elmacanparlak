# --- Player Data ---
stats = {
    "Health": 100,
    "Strength": 1,
    "Stamina": 1,
    "Friendship": 0,
    "Cuteness": 0,
    "Craftmanship": 1
}

inventory = {
    "Wood": 2,
    "Stone": 5,
    "Water": 2,
    "Flint": 1,
    "Food": 1
}

# --- Utility Functions ---
def show_inventory():
    print("\n=== INVENTORY ===")
    for item, amount in inventory.items():
        print(f"{item}: {amount}")

def show_stats():
    print("\n=== STATS ===")
    for stat, value in stats.items():
        print(f"{stat}: {value}")

def chop_wood():
    print("You chop down some wood. +5 Wood")
    inventory["Wood"] += 5

def forage_food():
    print("You forage and find a deer carcass. +5 Food")
    inventory["Food"] += 5

def search_coal():
    print("You wander into caves but get scared off. No coal found.")

def mine_stone():
    print("You crafted a wooden pickaxe and mined stones. +5 Stone")
    inventory["Stone"] += 5

# --- Character Creation ---
def character_creation():
    print("Choose your gender to start.")
    gender = input().lower()

    if gender in ["boy", "male", "guy", "man"]:
        name = input("Welcome aboard! Please state your name: ")
        print(f"Glad to see you here, {name}!")
        print("Choose your hairstyle: 1:Buzz Cut 2:Mullet 3:Mohawk 4:Low Taper Fade")
        hair = input()
        print("Choose your dress: 1:Braies 2:Hose 3:Doublet 4:Houppelande")
        dress = input()
        print("You are all set for your journey!")

    elif gender in ["girl", "woman", "female"]:
        name = input("Welcome aboard! Please state your name: ")
        print(f"Glad to meet you, {name}!")
        print("Choose your hairstyle: 1:Bobcut 2:Pixie 3:Shag Cut 4:Bangs")
        hair = input()
        print("Choose your dress: 1:Kirtle 2:Cotehardie 3:Surcote 4:Mantle")
        dress = input()
        print("You are all set for your journey!")

# --- Adventure Start ---
def start_adventure():
    print("Loading...\nPlease type 'goo' to continue")
    go = input()
    if go == "goo":
        print("Your adventure begins in an enormous forest full of trees.")
        print("Type 'inv' to see your resources.")
        if input() == "inv":
            show_inventory()
            print("Press '4' to light a fire.")
            if input() == "4":
                print("You lit a fire! -1 Wood, +1 Craftmanship")
                inventory["Wood"] -= 1
                stats["Craftmanship"] += 1
                print("Press '1' to see your stats")
                if input() == "1":
                    show_stats()
                print("You encounter a bunny. Options: Attack, Talk, Walk, Pet")
                action = input().lower()
                if action == "attack":
                    print("The bunny was a monster. You died.")
                elif action == "talk":
                    print("The bunny speaks! +2 Friendship")
                    stats["Friendship"] += 2
                elif action == "walk":
                    print("You walk past. Nothing happens.")
                elif action == "pet":
                    print("You pet the bunny. It meows. +1 Cuteness")
                    stats["Cuteness"] += 1

# --- Main Game Loop ---
def game_loop():
    while True:
        print("\nWhat would you like to do?")
        print("1: Inventory | 2: Stats | 3: Chop Wood | 4: Forage Food | 5: Search Coal | 6: Mine Stone | q: Quit")
        choice = input()

        if choice == "1":
            show_inventory()
        elif choice == "2":
            show_stats()
        elif choice == "3":
            chop_wood()
        elif choice == "4":
            forage_food()
        elif choice == "5":
            search_coal()
        elif choice == "6":
            mine_stone()
        elif choice == "q":
            print("Goodbye adventurer!")
            break

# --- Run Game ---
print("Welcome, Young and courageous adventurer!")
character_creation()
start_adventure()
game_loop()
