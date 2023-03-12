from typing import List


def find_two_sum(nums: List[int], target: int):
    p1, p2 = 0, 1
    number_of_elements = len(nums)

    for p1 in range(p1, number_of_elements):
        number_to_find = target-nums[p1]
        for p2 in range(p1+1, number_of_elements):
            if nums[p2] == number_to_find:
                return [p1, p2]

    return None


def find_two_sum(nums: List[int], target: int):
    nums_map = {}

    for index, value in enumerate(nums):
        if value not in nums_map:
            nums_map[target - value] = index
        else:
            return [nums_map[value], index]

    return None
