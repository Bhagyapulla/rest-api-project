def hashing_key(key,m):
    return key % m
m=8
print(f'the hash value for 4 is{hashing_key(4,m)}')
print(f'the hash value for 3 is{hashing_key(3,m)}')
print(f'the hash value for 10 is{hashing_key(10,m)}')
print(f'the hash value for 12 is{hashing_key(12,m)}')
print(f'the hash value for 8 is{hashing_key(8,m)}')

