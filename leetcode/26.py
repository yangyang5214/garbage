from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    length = len(nums)
    left, right = 1, 1
    while right < length:
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left = left + 1
        right = right + 1
    return left


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print("before: " + str(nums))
    remove_duplicates(nums)
    print("after: " + str(nums))
