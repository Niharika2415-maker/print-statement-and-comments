def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("pls select the operation")
print("a.add")
print("b.sub")
print("c.multiply")
print("d.divide")
choice= input("pls enter ur choice (a/ b/ c/ d):")
num1= int(input("enter the 1st number"))
num2= int(input("enter the 2nd number"))
if choice=='a':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='b':
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice=='c':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='d':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("this is an invalid input")
