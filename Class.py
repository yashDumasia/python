class Student:
    def __init__(abc,name,enrollment_no,cgpa):
        abc.name = name
        abc.enrollment_no = enrollment_no
        abc.cgpa = cgpa
        
    def show_name(abc):
        print("Name :",abc.name)
        
    def show_enrollment_no(abc):
        print("Enrollment No :",abc.enrollment_no)
        
    def show_cgpa(abc):
        print("cgpa :",abc.cgpa)

s1 = Student("Yash",250280152014,8.7)
s1.show_name()
s1.show_enrollment_no()
s1.show_cgpa()