import datetime
print("Enter First name")
f=input()
print("Enter last name")
l=input()
print("Enter DOB")
d=input()
print("Enter Dept")
dept=input()
print("Enter Phone No")
p=input()
c="Eli lilly"
name= f + " "+ l
dob = datetime.datetime.strptime(d, '%Y-%m-%d')
def from_dob_to_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

age = from_dob_to_age(dob)
print("Name :" + name)
print("Age :" , age)
print("DOB :",d)
print(c + "\n" + "department: ",dept)
print("Phone :",p)
