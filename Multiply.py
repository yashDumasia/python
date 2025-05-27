def multiply(*number):
    total = 1
    for number in number:
        total = total*number
    return total


print(multiply(2, 3, 4, 5))
