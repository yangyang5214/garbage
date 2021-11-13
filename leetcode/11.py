# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    s = Solution()
    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # arr = [1, 1]
    # arr = [4, 3, 2, 1, 4]
    # arr = [1, 2, 1]
    print(s.maxArea(arr))
