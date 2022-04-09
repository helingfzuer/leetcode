#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param m int整型
# @param n int整型
# @return int整型
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        for i in range(1, m):
            for j in range(0, n):
                if j == 0:
                    dp[j] = 1
                else:
                    dp[j] = dp[j-1] + dp[j]
        return dp[-1]


if __name__ == '__main__':
    m, n = int(input()), int(input())
    s = Solution()
    res = s.uniquePaths(m, n)
    print(res)