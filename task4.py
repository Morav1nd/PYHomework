import random

row1 = random.randint(2, 6)
print(row1)
row2 = random.randint(2, 6)
print(row2)
Fault = random.randint(1, 5)
print(Fault)
if Fault % row1 == 0 or Fault % row2 == 0:
    print('да')
else: print('нет')
