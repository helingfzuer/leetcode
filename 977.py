from operator import le
from posixpath import split
from turtle import right


class Solution:
    def sortedSquares(self, nums):
        left, right, pos = 0, len(nums)-1, len(nums)-1
        res = [0] * (len(nums))
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[pos] = nums[left]**2
                left += 1
            else:
                res[pos] = nums[right]**2
                right -= 1
            pos -= 1
        return res


if __name__ == '__main__':
    nums = [int(num) for num in input().split(' ')]
    s = Solution()
    nums = s.sortedSquares(nums)
    print(nums)