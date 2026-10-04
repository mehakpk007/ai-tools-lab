
def calculate_sum(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total


numbers = [10, 20, 30, 40, 50]

result = calculate_sum(numbers)
print("Sum =", result)
