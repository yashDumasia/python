high_income = True
good_credit = True
student = False
# and oprator
if high_income and good_credit == True:
    print("Eligible")
else:
    print("Not Eligible")
# or oprator
if high_income or good_credit == True:
    print("Eligible")
else:
    print("Not Eligible")
# not oprator
if not student == True:
    print("Eligible")
else:
    print("Not Eligible")
