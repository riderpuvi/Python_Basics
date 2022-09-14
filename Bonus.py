sal=int(input("Enter Your Salary"))
ten=int(input("Enter your Tenure"))
gross=0
if (ten>=10):
    gross=sal+(0.15*sal)
    print(gross)
elif(ten>=5 and ten<10):
    gross=sal+(0.10*sal)
    print(gross)
elif(ten>=3 and ten<5):
    gross=sal+(0.05*sal)
    print(gross)
else:
    print("Not eligible for Bonus but Sal={}".format(sal))
