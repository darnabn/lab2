vowels = ('a', 'e', 'i', 'o', 'i', 'u')

print(vowels.count('i'))

print(vowels.index('a'))

prime_numbers = {2, 3, 5, 7}

prime_numbers.add(11)
print(prime_numbers)

A = {1, 3, 5, 7, 9}
B = {2, 3, 5, 7, 11}

print(A.difference(B))

A = {2, 3, 5}
B = {1, 3, 5}

print('A U B = ', A.union(B))

numbers = {2, 3, 4, 5}

numbers.discard(3) 

print(numbers)