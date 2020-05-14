"""
look if number is repeated three or more times and when delete. Delete it by
index not to use remove as remove will delete from first found index and so index miss match can happen
"""


def remove_duplicates(self, nums: List[int]) -> int:
    i = 0
    while i < len(nums) - 2:
        prev = nums[i]
        if nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
            i += 2
            while i < len(nums) and nums[i] == prev:
                del nums[i]
        else:
            i += 1
    return len(nums)

