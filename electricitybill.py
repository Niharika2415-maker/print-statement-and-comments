unit= int(input("enter the number of units consumed"))
if (unit<50):
    amt=unit*2.60
    tax= 25
elif (unit<=100):
    amt= unit*3.25
    tax= 35
elif (unit<=200):
    amt= unit*5.26
    tax= 45
else:
    amt= unit*8.45
    tax= 75
total= amt-tax
print("total electricity bill",total)
