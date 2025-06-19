t= int(input("enter a nuumber"))
sum= 0
temp= t
while temp>0:
    digit= temp%10
    sum+=digit**3
    temp//=10
if t==sum:
    print(t,"is an armstrong number")
else:
    print("it is not an armstrong number")
     