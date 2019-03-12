dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())

numbers = [1, 2, 3]

# {1: 2, 2: 4, 3: 6}
print({n:n*2 for n in numbers})

# {2: 4}
print({n:n*2 for n in numbers if n%2 == 0})
