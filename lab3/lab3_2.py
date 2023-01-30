print("Enter command: ")
print("1. Integer typed list")
print("2. Char typed list")
print("3. String typed list")

a = int(input())


if(a == 1):
    arr1 = [1, 4, 2, 5, 2]
    for i in range(0, 5):
        print(arr1[i])

elif(a == 2):
    arr2 = ['H', 'o', 'e', 's', 's']
    for i in range(0, 5):
        print(arr2[i])

elif(a == 3):
    arr3 = ['Hi!', 'World', 'We', 'are', 'here']
    for i in range(0, 5):
        print(arr3[i])