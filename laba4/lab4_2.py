
n = int(input())
a = [0] * n

for i in range(len(a)):
    i = str(i + 1)
    print("Enter surnames: " + i)
    i = int(i)
    i = i - 1
    a[i] = str(input())

print()

m = int(input())
b = [0] * m
for i in range(len(b)):
    i = str(i + 1)
    print("Enter classes: " + i)
    i = int(i)
    i = i - 1
    b[i] = int(input())


print()

for i in range(len(a)):
    print(a[i], " ", end=" ")

print()

for i in range(len(b)):
    print(b[i], end=" ")
b.sort()

print()

for i in range(len(a)):
    print(a[i], " ", b[i])

