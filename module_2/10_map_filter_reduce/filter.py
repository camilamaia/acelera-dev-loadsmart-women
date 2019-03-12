# Filter Syntax: filter(function, iterable)

numbers = [-1, 0, 1, 2, 3, 4, 5]

filtered = filter(lambda x: x < 0, numbers)

print(list(filtered))
