str = str(input())
upper = 0
lower = 0

for i in str:
    if(i.islower()):
        lower += 1
    else:
        upper += 1

if(lower > upper):
    print(str.lower())
else:
    print(str.upper())