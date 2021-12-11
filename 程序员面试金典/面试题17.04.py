class Solution:
    def missingNumber(self, nums) -> int:
        res, n = 0, len(nums)
        for i in range(0, n):
            res = res ^ i ^ nums[i]
        return res ^ n


if __name__ == '__main__':
    nums = [int(num) for num in input().split(' ')]
    s = Solution()
    res = s.missingNumber(nums)
    print(res)