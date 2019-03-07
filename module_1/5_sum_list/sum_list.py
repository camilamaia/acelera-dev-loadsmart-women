def sum_list(numbers):
    index = 0
    total = 0

    while index < len(numbers):
        total += numbers[index]
        index += 1

    return total

def easy_sum_list(numbers):
    return sum(numbers)
