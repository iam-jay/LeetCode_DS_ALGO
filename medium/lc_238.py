"""
As question asked to avoid division so our approach is calculate
multiplication till that index excluding index from start and same from reverse
and then multiply each index so we have multiplication of indexes from left 
and from right excluding current index
"""


def product_except_self(nums: list[int]) -> list[int]:
    start_multiplier = [1]
    ending_multiplier = [1]
    multi = 1
    for i in range(len(nums)-1):
        multi = multi * nums[i]
        start_multiplier.append(multi)
    multi = 1
    for i in range(len(nums)-1, 0, -1):
        multi = multi * nums[i]
        ending_multiplier.append(multi)
    ending_multiplier.reverse()
    result = []
    for i in range(len(ending_multiplier)):
        result.append(start_multiplier[i]*ending_multiplier[i])
    return result
