print("Enter first string: ")

str1 = str(input())

print("Enter second string: ")

str2 = str(input())

print("Concat function: ")
def concat(str1, str2):
    print(str1 + str2)

print(concat(str1, str2), "\n")

print("Enter dublicating time: ")

n = int(input())
print("Dublicating function: ")

def duble(str1, n):
    print(str1 * n)

print(duble(str1, n), "\n")

print("Length function: ")
print(len(str1), " ", len(str2), "\n")

print("Replace function: ")
print("Old text: ")
txt = "I like playing football"
print(txt)
print("New text: ")
print(txt.replace("football", "games"), "\n")
print("Digit function: ", str1.isdigit())
print("Word function: ", str2.isalpha())
print("Lower function: ", str1.islower())
print("Upper function: ", str2.isupper())
print("Capitalize function: ", str1.capitalize(), " ", str2.capitalize())
print("Title function: ", str1.title(), " ", str2.title())








    



