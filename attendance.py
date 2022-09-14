n=input("Enter Student name")
c=int(input("No of Classes you attended "))
t=40
p=(c/t)*100
if(p>=80):
    print("Eligible")
else:
    print("Not Eligible")
