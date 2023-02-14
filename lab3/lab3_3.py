from random import randint, random, randrange

print("Enter command: 1, 2, 3, 4")

a = int(input())

if(a == 1):
    for i in range(randint(1, 15)):
        print(i)
elif(a == 2):
    for i in range(randrange(1,15, 3)):
        print(i)
elif(a == 3):
    for i in range(random * 10):
        print(i)
elif(a == 4):
    b = [1, 45, 3, 91, 2]
    print(list(enumerate(b)))

    




