def second_largest(numbers):
    numbers = sorted(set(numbers))
    print(numbers)
    return numbers[-2]

print(second_largest([100, 90, 80, 110, 70, 20, 10]))