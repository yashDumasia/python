import random
x = ["Head", "Tail"]
while True:
    choice = input("Toss(H/T) : ").upper()
    Toss = random.choice(x)
    if choice == "H":
        print("You chose Head")
    elif choice == "T":
        print("You chose Tail")
    else:
        print("Invalid Choice..!")
    print(f"Toss = {Toss}")
    if choice == "H" and Toss == "Head" or choice == "T" and Toss == "Tail":
        print("You won Toss.")
    else:
        print("You loss Toss.")
    play = input("Do you want to Toss agian...?(Y/N) : ").upper()
    if play == "Y":
        continue
    elif play == "N":
        break
    else:
        print("Invalid Choice..!")
        break
