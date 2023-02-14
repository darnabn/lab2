a = input()
b = input()
while not (a.isdigit() and b.isdigit()):
    a = input()
    b = input()

    
print(int(a) + int(b))
