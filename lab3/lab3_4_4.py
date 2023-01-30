n = int(input())
have = 0
for i in range(1, n+1):
    have+=i
for i in range(n - 1):
    have-=int(input())
print(have)