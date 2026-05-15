print("Welcome, Young and courageous adventurer! Your journey begins here. You will not stop in the face of summer, winter, hot and cold, through thick and thin and will continue to fight until the end")
print("Choose your gender to start.")
gender = input()
if gender == "boy" or gender == "male" or gender == "guy" or gender == "man":
     print("Welcome aboard! Please state your name.")
     name = input()
     print("Glad to see you here!",name,"\nPlease choose your hairstyle")
     print("1:Buzz Cut")
     print("2:Mullet")
     print("3:Mohawk")
     print("4:Low Taper Fade")
     hair = input()
     if hair == "1" or hair == "2" or hair == "3" or hair == "4":
         print("Wise choice young traveler! Let us dress you so that you won't feel cold")
         print("Choose your dress from 1-4")
         print("1:braies")
         print("2:hose")
         print("3:doublet")
         print("4:houppelande")
         dress = input()
         if dress == "1" or dress == "2" or dress == "3" or dress == "4":
             print("You are all set for your journey! Go on and show the world what you got!")
elif gender == "girl" or gender == "woman" or gender == "female":
        print("Welcome aboard! Please state your name.")
        name2 = input()
        print("Glad to meet you", name2, "\nPlease choose your hairstyle")
        print("1:Bobcut")
        print("2:Pixie")
        print("3:Shag Cut")
        print("4:Bangs")
        hair2 = input()
        if hair2 == "1" or hair2 == "2" or hair2 == "3" or hair2 == "4":
         print("Wise choice young traveler! Let us dress you so that you won't feel cold")
         print("Choose your dress from 1-4")
         print("1:Kirtle")
         print("2:Cotehardie")
         print("3:Surcote")
         print("Mantle")
         dress2 = input()
         if dress2 == "1" or dress2 == "2" or dress2 == "3" or dress2 == "4":
              print("You are all set for your journey! Go on and show the world what you got!")
print("Loading.....\n\n\nPlease type 'goo' to continue")
go = input()
print("Your adventure begins in an enormous forest full of trees.\nTo survive you need resources, Type 'inv' to see your resources.")
inv= input()
if inv == "inv":
    print("Wood: 2")
    print("Rock: 5")
    print("Water: 2 Liters")
    print("A flint")
    print("You have a lot to do. But everything begins with a fire and some sheen. Press '4' to light a fire.")
    fire = input()
    if fire == "4":
        print("You lit up a smoldering fire! Now you don't feel as cold.\nYou recieved the achievement of fire.\nPress '1' to see your stats")
        stats = input()
        if stats == "1":
            print("Craftmanship: Level 1\nOutdoormanship: Level 1(20% Progress)\n Strenght: Level 1\nStamina: Level 1\nArmory: Level 1")
            print("The night begins to creep as you are rifting through the forest. You encounter a harmless looking bunny.\nWhat do you do?\nAttack, Talk, Walk past, Pet.")
            action = input()
            if action == "Attack":
                print("The bunny was actually a hazardous monster. \nYou died.")
            elif action == "Talk":
                print("The bunny was actually was a subject of a spell. It talks back at you, uttering the words of mistery.\nYou gained 2 points of friendship.")
            elif action == "Walk Past":
                    print("Curiosity kills the cat. Nothing happened")
            elif action == "Pet":
                    print("You pet the cute bunny. It meows back at you. How? Nobody knows. You gained 1 points of cuteness.")

             

    
