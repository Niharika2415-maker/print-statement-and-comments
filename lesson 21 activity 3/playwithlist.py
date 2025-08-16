list= [11,12,13,14,15,21,22,23,24,25]
print("my list",list)
count= 0
for i in list:
    count+=i
average= count/len(list)
print("sum",count)
print("average",average)
list.sort()
print("smallest element is",list[0])
print("largest element is",list[-1])
