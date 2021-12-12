class Solution:
    def massage(self, nums) -> int:
        dp0, dp1 = 0, 0
        for num in nums:
            dp0, dp1 = dp1, max(dp1, dp0+num)
        return dp1


if __name__ == '__main__':
    nums = [int(num) for num in input().split(' ')]
    s = Solution()
    res = s.massage(nums)
    print(res)