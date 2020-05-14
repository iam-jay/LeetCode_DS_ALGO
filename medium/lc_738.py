
"""
Keep reducing by 1 from right to left from number whenever 
monotonic property is not satisfied. get last index where you reduced by 1
till that index from left to right copy number from original and replace 
other afterward by 9
"""


def monotone_increasing_digits(n: int) -> int:
    digits = str(n)
    result = []
    numbers = [0] * len(digits)
    for i in range(len(numbers)):
        numbers[i] = int(digits[i])
    index = len(numbers) - 1
    for i in range(len(numbers) - 1, 0, -1):
        if numbers[i] < numbers[i - 1]:
            numbers[i - 1] -= 1
            index = i - 1
    if numbers[0] != 0:
        for i in range(index + 1):
            result.append(str(numbers[i]))
        for i in range(index + 1, len(numbers)):
            result.append(str(9))
    else:
        for i in range(1, index + 1):
            result.append(str(numbers[i]))
        for i in range(index + 1, len(numbers)):
            result.append(str(9))
    return int("".join(result))
