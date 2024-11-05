a=(9,8,7,6,5,4,3,2,1)
b=(1,2,3,4,5,6,7,8,9)
dem=0
dict={}
for i in a:
    dict[i]=b[dem]
    dem+=1
print(dict)