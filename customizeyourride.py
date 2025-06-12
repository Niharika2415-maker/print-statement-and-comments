print("user kindly select your ride")
print("1.Bike")
print("2.Car")
t= int(input("choose your ride"))
if(t==1):
    print("what type of bike")
    print("1.Royal Enfield")
    print("2.BMW Bike")
    n= int(input("enter your choice"))
    if n==1:
        print("you have selected Royal Enfield")
    else:
        print("you have selected BMW Bike")
elif (t==2):
    print("what type of car you want")
    print("1.Sedan")
    print("2.SUV")
    m=int(input("enter your choice"))
    if m==1:
        print("you have selected Sedan")
    else:
        print("you have selected SUV")
else:
    print("your input is invalid")
     