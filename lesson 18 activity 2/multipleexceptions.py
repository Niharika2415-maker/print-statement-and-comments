try:
    num1,num2=eval(input("enter two numbers separated by a comma:"))
    result= num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("division by zero is error")
except SyntaxError:
    print("enter number separated by comma:")
except:
    print("wrong input")
else:
    print("no exception")
finally:
    print("this will execute no matter what")
    