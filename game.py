#game like snake,water,gun
import random as rand
option=["Snake","Water","Gun"]
option_selected=rand.choice(option)
print("""Welcome to the game
please Select one option
      1-->Snake
      2-->Water
      3-->Gun""")
num=int(input("Enter your option-->"))
if num==1 and option_selected=="Snake":
    print("tie")
elif num==1 and option_selected=="water":
    print("won")
elif num==1 and option_selected=="Gun":
    print("lost")
if num==2 and option_selected=="Snake":
    print("lost")
elif num==2 and option_selected=="water":
    print("tie")
elif num==2 and option_selected=="Gun":
    print("won")
if num==3 and option_selected=="Snake":
    print("won")
elif num==3 and option_selected=="water":
    print("lost")
elif num==3 and option_selected=="Gun":
    print("tie")
    
    