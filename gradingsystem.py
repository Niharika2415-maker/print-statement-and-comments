print("enter the the marks obtained in 5 subjects")
math= int(input("enter the marks scored in math"))
english= int(input("enter the marks scored in english"))
science= int(input("enter the marks scored in science"))
social= int(input("enter the marks scored in social"))
tamil= int(input("enter the marks scored in tamil"))
sum= math+english+science+social+tamil
avg= sum/5
if avg>=91 and avg<=100:
    print("your grade is A1")
elif avg>=81 and avg<=91:
    print("your grade is A2")
elif avg>=71 and avg<=81:
    print("your grade is B1")
elif avg>=61 and avg<=71:
    print("your grade id B2")
elif avg>=51 and avg<=61:
    print("your grade is C1")
elif avg>=41 and avg<=51:
    print("your grade is C2")
elif avg>=31 and avg<=41:
    print("your grade is D1")
elif avg>=21 and avg<=31:
    print("your grade is E1")
elif avg>=11 and avg<=21:
    print("your grade is E2")
else:
    print("fail")
