book_L = "Book.txt"
student_L = "Student.txt"

def Add_Book(title):
    with open(book_L,"a") as file:
      file.write(title + "\n")
    return f"\n✅ {title} Book is Added. ✅"
                
def View_Book():
    with open(book_L,"r") as file:
        lines = file.readlines()
    
    if len(lines) == 0:
        return "❌ Empty Library : No Books are in Library..!! ❌"
    
    print("")
    
    for lines in lines:
        print(lines,end="")
    
    print("")   
    
def Search_Book(title):
    
    title = title + "\n"
    
    with open(book_L,"r") as file:
        lines = file.readlines()
        
    if title in lines:
        print("\nBook Index : ",lines.index(title))
    else : 
        with open(student_L,"r") as file:
            lines = file.readlines()
            for lines in lines:
                if lines.split(" : ")[-1] == title:
                    print("Book was Borrow.")
                    return
        print("\n❌ Book is not in library. ❌")
    return

def Delete_Book(title):
    
    with open(book_L,"r") as file:
        lines = file.readlines()
        
    found = False
    
    with open(book_L,"w") as file:
        for i in lines:
            if i.strip() != title:
                file.write(i)
            else:
                found = True

    if found == False:
        return False
    else:
        return True

def Issue_Book(student,book):
    
    if Delete_Book(book) == True:
        with open(student_L,"a") as file:      
            file.write(student + " : " + book + "\n")
        print("\n✅ Data Enter Successfully. ✅")
    else :
        print(f"\n❌ {book} is not in Library. ❌")

def Return_Book(student,book):
    
    with open(student_L,"r") as file:
        lines = file.readlines()
        
    found = False
    with open(student_L,"w") as file:
        for i in lines:
            if i.strip() != student + " : " + book:
                file.write(i)
            else:
                found = True
                Add_Book(book)  
                print("\n✅ Book Return to Library. ✅")
    if found == False:
         print("\n❌ Student or Book not found..!! ❌")
     
def View_Students():
    
    with open(student_L,"r") as file:
        lines = file.readlines()
    
    print("")
    
    for lines in lines:
        print(lines,end="")
    
    print("")
      
def main():
    print("\n===================================")
    print("    LIBRARY MANAGEMENT SYSTEM")
    print("===================================")
    print("\nWelcome To Library Management System.\n")
    
    print(" 1. Add Book \n 2. View Books \n 3. Search Book \n 4. Delete Book \n 5. Issue Book \n 6. Return Book \n 7. View Students\n 0. Exit")
        
    while True:
        
        print(" ")
        choice = input("Enter Your Choice : ")
        
        if choice == "1":
            title = input("\nEnter Book Name : ")
            Add_Book(title)
            print("✅ Book Added Successfully. ✅")
        
        elif choice == "2":
            print("\n===================================")
            print("        -: Books📕 Name :-")
            print("===================================\n")
            View_Book()
        
        elif choice == "3":
            title = input("\nEnter Book Name : ")
            Search_Book(title)
        
        elif choice == "4":
            title = input("\nEnter Book Name : ")
            if Delete_Book(title) == True:
                print(f"\n✅ {title} is Deleted from Library. ✅")
            else:
                print(f"\n❌ {title} is not in Library. ❌")
            
        elif choice == "5":
            student = input("\nEnter Student Name : ")
            title = input("Enter Book Name : ")
            Issue_Book(book=title,student=student)
            
        elif choice == "6":
            student = input("\nEnter Student Name : ")
            title = input("Enter Book Name : ")
            Return_Book(book=title,student=student)
            
        elif choice == "7":
            print("\n===================================")
            print("     -: Students🧑‍🎓 Detail :-")
            print("===================================\n")
            print("Student Name  :  Book Name")
            View_Students()
                    
        elif choice == "0":
            print("\n🙏 Thank You 🙏")
            break
        
        else :
            print("\n❌ Invalid Choice..!! ❌")
    
def password(): 
    username = input("Enter Your Username : ")
    password = input("Enter Your Password : ")

    if username == "Yash" and password == "Yash1897":
        main()
    else:
        print("❌ Incorrect Username or Password...!! ❌")

password()