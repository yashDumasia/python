T = "Task.txt"

def add_task():
  y = 0
  x = int(input("How many task you want to add : "))
  while True:
    task = input("Add Task : ")
    with open(T,"a") as file:
        file.write(task+"\n")
    print("Task Added.✅")
    y = y + 1
    if x == y:
      break
    else:
      continue 

def show_task():
  with open(T, "r") as file:
      lines = file.readlines()
      if not lines:
            print("No Task Added.❌")
      else:
        print("Your Tasks :")
        for line in lines:
          print("-", line.strip())

def mark_task():
 while True:
    mark = input("Enter The Task number to mark as done(if not, enter 0) : ")
    if mark == "0":
      break
    else:
      with open(T,"a") as file:
        file.write("Task"+" "+mark+" "+"completed.👍"+"\n")
    
def clear_task():
  with open(T,"w") as file:
    print("Task History is Cleared.👍")
  
while True:
  print("====== To Do List ====== ")
  print("1. Add Task")
  print("2. Show Task")
  print("3. Mark Task as Done")
  print("4. Clear Task History")
  print("5. Exit")

  
  choice = int(input("Enter Choice : "))
  if choice == 1:
    add_task()
  elif choice == 2:
    show_task()
  elif choice == 3:
    mark_task()
  elif choice == 4:
    clear_task()
  elif choice == 5:
    break
  else:
    print("❌ Invalid Choice ..! ❌")
    break
  print("\n")