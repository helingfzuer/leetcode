class Solution:
    def findLength(self, nums1, nums2):
        n1, n2, res = len(nums1), len(nums2), 0
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                dp[i][j] = dp[i-1][j-1]+1 if nums1[i-1] == nums2[j-1] else 0
                res = max(dp[i][j], res)
        return res


if __name__ == '__main__':
    nums1 = [int(num) for num in input().split(' ')]
    nums2 = [int(num) for num in input().split(' ')]
    s = Solution()
    res = s.findLength(nums1, nums2)
    print(res)