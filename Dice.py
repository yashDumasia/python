import random
while True:
    choice = input("Roll the Dice(y/n)...? : ")
    if choice.lower() == "y":
        dice1 = random.randint(1, 6)
        print(f"({dice1})")
    elif choice.lower() == "n":
        print("Thanks for playing")
        break
    else:
        print("Invalid Choise...! ")
