#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param cost int整型一维数组
# @return int整型
#
class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        n = len(cost)
        dp0, dp1 = 0, 0
        for i in range(2, n+1):
            dp0, dp1 = dp1, min(cost[i-2]+dp0, cost[i-1]+dp1)
        return dp1


if __name__ == '__main__':
    costs = [int(cost) for cost in input().split(' ')]
    s = Solution()
    res = s.minCostClimbingStairs(costs)
    print(res)