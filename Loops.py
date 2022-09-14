"""

n=(0,1,2,3,4)
s=0
for i in n:
    s=s+i
print(s)
"""

list=["Name","Phone","age","sal"]

for i in list:

    if(i=="Name"):

        name = input("Enter your first name \n")

        if(name.isalpha()):

            print(f"Valid {i}\n")

        else:

            print(f"Not valid {i}")

    elif(i=="Phone"):

        phone = input("Enter your phone\n")

        if phone.isnumeric() and len(phone)==10:

            print(f"Valid {i}\n")

        else:

            print(f"Not valid {i}")   
        
    elif(i=="age"):

        age = input("Enter your age\n")

        if age.isnumeric() and (int(age)>=20 and int(age)<=60):

            print(f"Valid {i}\n")

        else:

            print(f"Not valid {i}")

    elif(i=="sal"):

        sal = input("Enter your sal\n")

        if sal.isnumeric() and int(sal)>=10000:

            print(f"Valid {i}\n")

        else:

            print(f"Not valid {i}")
