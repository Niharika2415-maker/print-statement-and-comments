height= int(input("enter your height in cm"))
weight= int(input("enter your weight in kg"))
bmi= weight/(height/100)**2
print("your bmi is",bmi)
if bmi <=18.4:
    print("you are under weight")
elif bmi<=24.9:
    print("you are healthy")
elif bmi<=29.9:
    print("you are over weight")
elif bmi<=34.9:
    print("you are severly over weight")
elif bmi<=39.9:
    print("you are obese")
else:
    print("you are severly obese")
    