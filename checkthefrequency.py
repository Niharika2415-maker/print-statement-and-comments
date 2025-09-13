test_dict={'Nithvika' : 24, 'is' : 24, 'a' : 22, 'smart' : 11, 'child' : 24}
print("the original dictionary"+str(test_dict))
k= 11
res=0
for key in test_dict:
    if test_dict[key]==k:
        res= res+1
print("frequeny of k is "+str(res))
