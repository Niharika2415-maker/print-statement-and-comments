num= input("enter the number")
length=len(num)
if length%2!=0:
    middle= int(num[length//2])
    print("middle digit product",middle)
else:
    mid1= int(num[length//2-1])
    mid2= int(num[length//2])
    product= mid1*mid2
    print("middle digits are",mid1,"and",mid2)
    print("product of middle digits is",product)
    