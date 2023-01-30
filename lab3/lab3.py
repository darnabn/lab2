print("Enter command: 1 or 2")
x = int(input())

print()
print("Enter a:")
a = int(input())
print("Enter b: ")
b =int(input())
print()

if(x == 1):
    print("You choose for:")
    for i in range(a, b):
        print(i)

elif(x == 2):
    print("You choose while: ")
    i = a
    while(i < b):
        print(i)
        i += 1