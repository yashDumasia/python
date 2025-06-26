import random
food = ["apple","banana","mango","watermelon","vadapav","bhajipav","dhosa","manchuriyan","noddles","khichadi","roti","sabji","ladu","halwa","gulabjamun","rasgulla","dabeli"]
animal = ["tiger","lion","monkey","cat","cow","dog","buffalo","zebra","deer","cheetah","elephant","horse","parrot","pinggen","sparrow","snake","parrot","peacock","ant","fly","butterfly","spyder","dove"]
countries = ["australia","newzealand","india","pakistan","nepal","america","japan","china","africa","bangladesh","usa","afghanistan","england","westindies","bhutan",]

print("WELLCOME TO THE NAME GUESSING GAME.\n")
level = input("Chose Name(Food/Animal/Countries(F/A/C)) : ").upper()

if level == "F":
    Name = random.choice(food)
elif level == "A":
    Name = random.choice(animal)
elif level == "C":
    Name = random.choice(countries)
else :
    print("Invalid choice. and Defalting to food name.\n")
    Name = random.choice(food)

attemps = 0
print("Guess a Name\n")

while True:
   
    guess = input ("Enter Name : ").lower()
    attemps = attemps + 1 
    if guess == Name :
        print (f"You guess Name in {attemps} attemps.")
        break
    hint = ("")

    for i in range(len(Name)):
        if i < len(guess) and guess[i] == Name[i]:
            hint = hint+guess[i]
        else:
            hint = hint + "_"
    print(f"Hint : {hint}")
print("GAME OVER..!!")
        