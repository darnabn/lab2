print("Make resume: ")
print("Enter your name: ")
name = str(input())

print("Enter your surname: ")
surname = str(input())

print("Enter your age: ")
age = int(input())

a = [f"Name: {name}", f"Surname: {surname}", f"Age: {age}" ]

while True:
    print("Do you want to add some information? ")
    print("Enter y[yes] or n[no]: ")
    c = input()
    if(c == 'y'):
        print("Enter kind of information: ")
        type = input()
        info = input()
        a.insert(4, f"{type}: {info}")
        print("Information added!")
        while True:
            print("Do you want to add some information? ")
            print("Enter y[yes] or n[no]: ")
            c = input()
            if(c == 'y'):
                print("Enter kind of information: ")
                type = input()
                info = input()
                a.append(f"{type}: {info}")
                print("Information added!")
                print("Do you want to delete some information?")
                print("Enter y[yes] or n[no]:")
                c1 = input()
                if(c1 == 'y'):
                    print("Enter position")
                    c1_1 = int(input())
                    a.pop(c1_1)
                elif(c1 == 'n'):
                    print(a.copy())

            if(c == 'n'):
                break
                    
    if(c == 'n'):
        print(a)
        break

print("Do you want to delete? ")
print("Enter yes or no: ")
c2 = input()
if(c2 == 'y'):

    a.clear()
    print(a)
elif(c2 == 'n'):
    print(a.copy())





        



