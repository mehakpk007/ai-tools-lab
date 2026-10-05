def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        middle = (low + high) // 2

        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1


numbers = [10, 20, 30, 40, 50]
target = 30

result = binary_search(numbers, target)

print("Target found at index:", result)