History = "History.txt"

def show_history():
    with open(History,"r") as file:
      lines = file.readlines()
      if not lines:
         print("No History Found...!!")
      else:
         for lines in lines:
            print(lines)
    
def clear_history():
    file = open(History,"w")
    file.close()
    print("History Cleared.")

def save_history(equation,result):
    with open(History,"a") as file:
       file.write(equation + " = " + str(result) + "\n")
     
def calculator(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print ("Invalid Input...!!(Use Formate = number + operator + number (example = 8 + 8))")
        return
    num1 = float(parts[0])
    ope = parts[1]
    num2 = float(parts[2])

    if ope == "+":
        result = num1 + num2
    elif ope == "-":
        result = num1 - num2
    elif ope == "*":
        result = num1 * num2
    elif ope == "/":
        if num2 == 0:
            print("Can't Devide By 0...!")
            return
        else:
           result = num1 / num2
    elif ope == "//":
        if num2 == 0:
            print("Can't Devide By 0...!")
            return
        else:
           result = num1 // num2
    else:
        print("Invalid operator..!(Use + , - , * , /,//) ")
        return
    if int(result) == result:
        result = int(result)
    print(f"Result = {result}")
    save_history(user_input,result)
    
def main():
    print("SIMPLE CALCULATOR \n")
    while True:
        user_input = input("Enter Calculation(+,-,*,/,//) or h(history),c(clear),e(exit) : ")    
        if user_input.upper() == "H":
            show_history()
        elif user_input.upper() == "C":
            clear_history()
        elif user_input.upper() == "E":
            print("Thanks For Use Calculator. Good Bye..!")
            break
        else :
            calculator(user_input)

main()
   