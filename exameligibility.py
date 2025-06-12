t= input("does the student have medical conditions Y or N")
n= int(input("what is the attendance percentage of the student "))
if t=='Y':
    print("you are eligible for the examination")
else:
    if n>=75:
        print("you are eligible for the examination")
    else:
        print("you are not eligible for the examination")
        