list1 = input()
list2 = list(list1)
flag = 0
i = 1
while i < len(list1):
    if(list1[i] < list1[i - 1]):
        flag = 1
    i += 1
if (not flag) :
    print ("True")
else :
    print ("False")
