# Without Reduce
product = 1
numbers = [1, 2, 3, 4]
for num in numbers:
    product = product * num

# With Reduce

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
