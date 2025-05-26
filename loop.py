succesfull = True

for number in range(3):
    print("Attemp", number+1)
    if succesfull == True:
        print("Succesfull")
        break
else:
    print("Attempted 3 times but Failed")
