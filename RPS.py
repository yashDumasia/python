import random
X = ["Rock🪨", "Paper📃", "Scissor✂️"]
while True:
    computer = random.choice(X)
    choice = input("Rock,Paper and Scissor(R,P and S)...? : ").upper()

    if choice == "R":
        print("Your Chose Rock🪨")
    elif choice == "P":
        print("Your Chose Paper📃")
    elif choice == "S":
        print("Your Chose Scissor✂️")
    else:
        print("Invalid Choice..!")
        break

    if computer == "Rock🪨":
        print("Computer Chose Rock🪨")
    elif computer == "Paper📃":
        print("Computer Chose Paper📃")
    elif computer == "Scissor✂️":
        print("Computer Chose Scissor✂️")

    if choice == "R" and computer == "Scissor✂️" or choice == "P" and computer == "Rock🪨" or choice == "S" and computer == "Paper📃":
        print("You Won.")
    elif choice == "R" and computer == "Rock🪨" or choice == "P" and computer == "Paper📃" or choice == "S" and computer == "Scissor✂️":
        print("Tied.")
    else:
        print("You Lose.")

    Y = input("Do You Want To Play Again...?(Y/N) : ").upper()
    if Y == "Y":
        continue
    elif Y == "N":
        break
    else:
        print ("Invalid Choice..!!")
        break
