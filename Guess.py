import random
Number = random.randint(1, 100)
while True:
    try:
        Guess = int(input("Guess a Number Between 1 to 100 : "))

        if Guess < 0 or Guess > 100:
            print("Invalide Number..!")
        elif Number > Guess:
            print("It's Smaller..!")
        elif Number < Guess:
            print("It's Bigger..!")
        elif Number == Guess:
            print("Congratulation!, You Guess Right Number. ")
            break

    except ValueError:
        print("Please Enter Valid Number..!")
