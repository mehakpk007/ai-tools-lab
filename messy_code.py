def calculate_average(numbers, count):
    """Calculate the average of a list of numbers."""
    if count == 0:
        raise ValueError("Count cannot be zero.")

    total = 0

    for number in numbers:
        total += number

    return total / count


numbers = [10, 20, 30]
average = calculate_average(numbers, len(numbers))
print(average)