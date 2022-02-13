import collections


class Solution:
    def sumOfUnique(self, nums) -> int:
        dic = collections.Counter(nums)
        return sum(num for num, cnt in dic.items() if cnt == 1)

if __name__ == '__main__':
    nums = [int(num) for num in input().split(' ')]
    s = Solution()
    res = s.sumOfUnique(nums)
    print(res)