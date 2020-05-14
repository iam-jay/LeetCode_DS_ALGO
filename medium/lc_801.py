"""
This is typical DP problem where at each index you have choice to swap keep 
strictly increasing sequence.
Calculate what would be cost if we have choice to swap or don't swap at index 
i from i-1
"""


def min_swap(a: list[int], b: list[int]) -> int:
    no_swap = [0] * len(a)
    swap = [1] * len(a)
    for i in range(1, len(a)):
        no_swap[i] = swap[i] = len(a)
        """
        At this place we don't need swap but what would be cost to reach till this index. And what if we swap here then what would be cost.
        """
        if a[i - 1] < a[i] and b[i - 1] < b[i]:
            no_swap[i] = no_swap[i - 1]
            swap[i] = swap[i - 1] + 1
        """
        We here not sure if we need to swap or not so what would be cost if we need to swap or cost if we don't need to swap
        """
        if a[i] > b[i - 1] and b[i] > a[i - 1]:
            no_swap[i] = min(no_swap[i], swap[i - 1])
            swap[i] = min(swap[i], no_swap[i - 1] + 1)

    return min(no_swap[-1], swap[-1])
