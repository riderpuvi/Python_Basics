
name=input("Enter your name : ")
while len(name)==0 or name.isalpha()== False:
     name=input("Enter Name which has only alphabets and Not empty : ")

phone=input("Enter phone Number : ")
while len(phone)!=10 or phone.isnumeric()==False:
    phone=input("Enter Valid Telephone Number : ")

age=input("Enter Your Age : ")
while int(age)<20 or int(age)>100  or age.isnumeric()==False:
     age=(input("Enter Valid Age : "))

sal=input("Enter your salary : ")
while  len(sal)==0 or  sal.isnumeric()==False or int(sal)<0:
    sal=input("Enter Valid salary: ") 

city=input("Enter your city: ")
while city.isalpha()==False or len(city)==0:
    city=input("Enter valid City name: ")

dept=input("Enter Your Department: ")
while len(dept)==0 or dept.isalpha()==False:
    dept=input("Enter Valid Department: ") 

print("\nName:", name)
print("Phone:", phone)
print("Age:", age)
print("Sal:", sal)
print("City:", city)
print("Dept:", dept)

