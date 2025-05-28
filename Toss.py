import random
while True:
    choice = input("Toss(y/n) : ")
    if choice.lower() == "y":
        Toss = random.randint(1, 2)
        if Toss == 1:
            print("Head")
        else:
            print("Tail")
    elif choice.lower() == "n":
        print("Thanks for playing")
        break
    else:
        print("Invalid Choise...! ")
