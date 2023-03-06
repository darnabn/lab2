import random

tpl_1 = tuple(random.randint(0, 5) for i in range(10))
tpl_2 = tuple(random.randint(-5, 0) for i in range(10))
tpl_3 = tpl_1 + tpl_2

count = 0
for i in tpl_3:
    if i == 0:
        count += 1
print("tuple:", tpl_3)
print("count of 0:", count)
