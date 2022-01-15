from math import gcd
a = input()
a=a.split(' ')
b=[]
for i in a:
    b.append(int(i))
if len(b) ==0:
    print(b[0])
div = gcd(b[0], b[1])
if len(b) == 2:
    print(div)
for i in range(1, len(b) - 1):
      div = gcd(div, b[i + 1])
if div == 1:
    print(div)
print(div)
