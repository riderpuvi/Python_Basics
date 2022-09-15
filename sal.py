import cal
f_name=input("Enter your first name")
l_name=input("Enter your last name")
s=cal.takesalary()
hra=cal.HRA(s)
da=cal.DA(s)
bonus=cal.bonus(s)
print("Total Salary :", s+hra+da+bonus) 
