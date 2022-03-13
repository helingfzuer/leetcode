class Solution:
    def goodDaysToRobBank(self, security, time: int):
        n = len(security)
        left, right = [0]*n, [0]*n
        for i in range(1, n):
            if security[i] <= security[i-1]:
                left[i] = left[i-1] + 1
        for i in range(n-2, 0, -1):
            if security[i] <= security[i+1]:
                right[i] = right[i+1] + 1
        return [i for i in range(time, n-time) if left[i] >= time and right[i] >= time]


if __name__ == '__main__':
    nums = [int(num) for num in input().split(' ')]
    time = int(input())
    s = Solution()
    res = s.goodDaysToRobBank(nums, time)
    print(res)