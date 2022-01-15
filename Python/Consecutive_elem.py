a= [1,1,1,2,2,1,4,4,5,3,6,2,2,2,2,4]
len(a)
d=[]
for index in range(0,len(a)-1):
    if a[index] == a[index+1]:
        d.append(a[index])
d=len(list(set(d)))
print(d)
