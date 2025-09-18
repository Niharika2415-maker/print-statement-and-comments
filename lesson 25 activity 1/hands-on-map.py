a= [12,11,24]
b= [10,22,5]
result= map(lambda x,y:x+y,a,b)
print("addition if two lists",list(result))
c= [20,25,9]
def squares(n):
    return n*n
square= list(map(squares,c))
print("square of numbers in the list",square)