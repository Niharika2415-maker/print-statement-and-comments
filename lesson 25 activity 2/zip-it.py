a= {13,24,11,3}
b= {22,5,20,21}
c= list(zip(a,b))
print("zipped list from two lists is ",c)
d= [44,4,5,6]
e= [8,9,10,11]
for x,y in zip(d,e[::-1]):
    print("second list in reverse order",(x,y))
name= ['Lakshmitha','Josika','Akshara']
rollno= [34,28,18]
dict= {name:rollno for name,rollno in zip(name,rollno)}
print('\n{}'.format(dict))
