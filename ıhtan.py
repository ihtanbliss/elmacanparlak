print("Welcome aboard, courageous warrior. Type start to begin your adventure!")
answer = input()
if answer == "start":
    print("You embarekd on a new journey. Let us create you a character.")
    print("What is your sex?")
    gender = input()
    if gender == "Female":
        print("Please choose your hairstyle from 1-4")
        print("1:Pixie")
        print("2:Bob cut")
        print("3:Braid")
        print("4:Afro")
    hair = input()
    if hair == "1" or hair == "2" or hair == "3" or hair == "4":
             print("Good choice, warrior! Let us dress you so you will not feel cold!")
             print("Please choose yourself a dress from 1-3")
             print("1:kirtle")
             print("2:chemise")
             print("3:houppelande")
    dress = input()
    if dress == "1" or "2" or "3":
        print("You are all set young adcenturer! Go out there and show the world what you got!")
elif gender == "Male":
        print("Please choose your hairstyle from 1-4")
        print("1:Mohawk")
        print("2:Mullet")
        print("3:Buzz Cut")
        print("4:Low Taper Fade")
        hair2 = input()
elif hair2 == "1" or hair2 == "2" or hair2 == "3" or hair2 == "4":
        print("Good choice, warrior! Let us dress you so you will not feel cold.")
        
        
