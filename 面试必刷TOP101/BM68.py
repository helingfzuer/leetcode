#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param matrix int整型二维数组 the matrix
# @return int整型
#
class Solution:
    def minPathSum(self, matrix) :
        n, m = len(matrix), len(matrix[0])
        dp = [[0]*m]*n
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[i][j] = matrix[i][j]
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1] + matrix[i][j]
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i-1][j] + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
        return dp[-1][-1]


if __name__ == '__main__':
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append([int(num) for num in input().split(' ')])
    s = Solution()
    res = s.minPathSum(matrix)
    print(res)