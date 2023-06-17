#решение 1
import random

a = random.randint(100, 1000)
print(type(a))
print(a)

b = str(a)
print(type(b))
print(b)
 
sum = int(b[0]) + int(b[1]) + int(b[2])
print(type(sum))
print(sum)

print('----------')
#решение 2

c = input()
print(type(c))
print(c)
summa = int(c[0]) + int(c[1]) + int(c[2])
print(summa)