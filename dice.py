import random

def dice(): 
    while True:  
          number =  random.randint(1, 6)
          print(number)
          if 1 <= number <= 2:
               print("Ouch... Bad luck")
          elif 3 <= number <= 4:
               print("Good, very good.")
          elif 5 <= number <= 6:
               print("Awesome! You got incredible lucky!")
          
          ans = input("Do you want to roll again?(y/n)")
          if ans == "y":
           pass
          elif ans == "n":
              print("Okay, exiting the dice roller. Goodbye now!")
              break
   

dice()







