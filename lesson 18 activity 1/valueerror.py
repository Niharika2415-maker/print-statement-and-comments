try:
    number=int(input("enter a number:"))
    print("the entered number is",number)
except ValueError as ex:
    print("exception",ex)
    