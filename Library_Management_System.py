book_L = "Book.txt"
student_L = "Student.txt"

def Add_Book(title,id = "-",author = "-"):
    with open(book_L,"a") as file:
      file.write(title+ " : " + id + " : " + author + "\n")
    return 
                
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
    
    found = False
    x = 0
    with open(book_L,"r") as file:
        for line in file:
            if line.strip().split(" : ")[0] == title:
                print(f"\nBook Index : {x}")
                found = True
                return
            else:
                x += 1
                
    if found == False:
        with open(student_L,"r") as file:
            for line in file:
                if line.strip().split(" : ")[2] == title:
                    print("\nBook was Borrow.")
                    return
                    
    print("\n❌ Book is not in library. ❌")
    return

def Delete_Book(title):
    
    found = False

    with open(book_L, "r") as file:
        lines = []

        for line in file:
            if line.strip().split(" : ")[0] != title:
                lines.append(line)
            else:
                found = True

    with open(book_L, "w") as file:
        for line in lines:
            file.write(line)

    return found

def Issue_Book(student,book,student_detail = "-"):
    
    x = ""    
    with open(book_L,"r") as file:
        lines = []
        for line in file:
            if line.strip().split(" : ")[0] == book:
                lines.append(line)
                Delete_Book(line.strip().split(" : ")[0]) # Remove from Book.txt file

                 
              
    for str in lines:
        x = x + str + " : "
      
    if len(lines) == 0:
        print(f"\n❌ {book} is not in Library. ❌")

    else:       
        with open(student_L,"a") as file:
            file.write(student + " : " + student_detail+ " : " + x[:-3]) # Adding in Student.txt file
        print("\n✅ Data Enter Successfully. ✅")           
    
def Return_Book(student,book):
    
    lines = []
    y = ""
    
    with open(student_L, "r") as file:

        for line in file:
            if line.strip().split(" : ")[0] != student and line.strip().split(" : ")[2] != book:
                lines.append(line)
            else:
                y = y + line

    with open(student_L, "w") as file:
        for line in lines:
            file.write(line)
            
    if y != "":
        with open(book_L,"a") as file:
            file.write(y.strip().split(" : ")[2] + " : " + y.strip().split(" : ")[3] + " : " + y.strip().split(" : ")[4] + "\n")
            print("\n✅ Book Return to Library. ✅")
    else:
        print("\n❌ Student or Book not found..!! ❌")
           
def View_Students():
    
    with open(student_L,"r") as file:
        lines = file.readlines()
    
    print("")
    
    for lines in lines:
        print(lines,end="")
    
    print("")

def Book_ID(title):
    lines = ""
    found = False
    with open(book_L,"r") as file:
        for line in file:
            if line.strip().split(" : ")[0] == title:
                lines = line
                found = True
                
    if found == True:
        print("\nBook ID : ",lines.strip().split(" : ")[1])    
    else :
        with open(student_L,"r") as file:
            for line in file:
                if line.strip().split(" : ")[2] == title:
                    lines = line
                    found = True
                
        if found == True:
            print("\nBook ID : ",lines.strip().split(" : ")[3],"(Borrowed)")
        else :
            print("\n❌ Book is not in library. ❌")

def Student_Info(name):

    with open(student_L,"r") as file:
        for line in file:
            if line.strip().split(" : ")[0] == name:
                print("\nStudent Std/Div    : ",line.strip().split(" : ")[1])
                print("Borrowed Book Name : ",line.strip().split(" : ")[2])
                print("Book ID            : ",line.strip().split(" : ")[3])
                print("Book's Author Name : ",line.strip().split(" : ")[4])
                return
    
    print("\n❌ Student not Found..!! ❌")
    return                

def Book_Info(title):
    
    with open(book_L,"r") as file:
        for line in file:
            if line.strip().split(" : ")[0] == title:
                print("\nBook ID            : ",line.strip().split(" : ")[1])
                print("Book's Author Name : ",line.strip().split(" : ")[2])
                print("Book Status        :  Book In Library")
                return
            
    with open(student_L,"r") as file:
        for line in file:
            if line.strip().split(" : ")[2] == title:
                print("\nBook ID            : ",line.strip().split(" : ")[3])
                print("Book's Author Name : ",line.strip().split(" : ")[4])
                print(f"Book Status        :  Book Borrow by {line.strip().split(" : ")[0]}")
                return
            
    print("\n❌ Book not Found..!! ❌")
    return

def main():
    
    print("\n======================================")
    print("📘📕 LIBRARY🏬 MANAGEMENT SYSTEM 📘📕")
    print("======================================")
    print("\nWelcome To Library Management System.\n")
    
    print(" 1. Add Book 📕 \n 2. View Books 📖 \n 3. Search Book 🔍 \n 4. Delete Book 🗑️ \n 5. Issue Book 📤 \n 6. Return Book 📥 \n 7. View Students 🧑 \n 8. Book ID📕 \n 9. Student Information 🧑‍🎓 \n 10. Book Infomation 📘 \n 0. Exit()")
        
    while True:
        
        print(" ")
        choice = input("Enter Your Choice : ")
        
        if choice == "1":
            title = input("\nEnter Book Name : ")
            id = input("Enter Book id : ")
            author = input("Enter Author Name : ")
            Add_Book(title.strip(),id.strip(),author.strip())
            print("\n✅ Book Added Successfully. ✅")
        
        elif choice == "2":
            print("\n===================================")
            print("        -: Books📕 Name :-")
            print("===================================\n")
            print("Book Name : Book ID : Author Name")
            View_Book()
        
        elif choice == "3":
            title = input("\nEnter Book Name : ")
            Search_Book(title.strip())
        
        elif choice == "4":
            title = input("\nEnter Book Name : ")
            if Delete_Book(title.strip()) == True:
                print(f"\n✅ {title} is Deleted from Library. ✅")
            else:
                print(f"\n❌ {title} is not in Library. ❌")
            
        elif choice == "5":
            student = input("\nEnter Student Name : ")
            student_detail = input("Enter Student Standard and Division (Std/Div) : ")
            title = input("Enter Book Name : ")
            Issue_Book(book=title.strip(),student=student.strip(),student_detail=student_detail.strip())
            
        elif choice == "6":
            student = input("\nEnter Student Name : ")
            title = input("Enter Book Name : ")
            Return_Book(book=title.strip(),student=student.strip())
            
        elif choice == "7":
            print("\n===================================")
            print("     -: Students🧑‍🎓 Detail :-")
            print("===================================\n")
            print("Student Name : Std/Div : Book Name : Book ID : Author Name")
            View_Students()
                  
        elif choice == "8":
            book = input("\nEnter Book Name : ")
            Book_ID(book.strip())
          
        elif choice == "9":
            student = input("\nEnter Student Name : ")
            Student_Info(student.strip())
            
        elif choice == "10":
            book = input("\nEnter Book Name : ")
            Book_Info(book.strip())
          
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