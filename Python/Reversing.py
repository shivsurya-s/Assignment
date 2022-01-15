a=int(input('Enter a number:'))
revsed = 0
while a > 0:
    r= a % 10
    revsed = (revsed*10) + r
    a = a // 10
print('Reverse of Integer',revsed)
