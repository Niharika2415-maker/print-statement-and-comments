import array as arr
array1= arr.array('i',[1,3,5,3,7,9,3])
print("original array"+str(array1))
print("no.of occurences of 3 in array"+str(array1.count(3)))
array1.reverse()
print("the reverse "+str(array1))