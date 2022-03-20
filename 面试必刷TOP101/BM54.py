#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @return int整型二维数组
#
class Solution:
    def threeSum(self, num):
        res = []
        num.sort()
        for i, n in enumerate(num):
            if i > 0 and num[i] == num[i-1]:
                continue
            left, right = i+1, len(num)-1
            while left < right:
                if num[left] + num[right] + n == 0:
                    tmp = [n, num[left], num[right]]
                    res.append(tmp)
                    left, right = left+1, right-1
                    while left < right and num[left] == num[left-1]:
                        left = left+1
                    while left < right and num[right] == num[right]+1:
                        right = right-1
                elif num[left] + num[right] + n < 0:
                    left = left + 1
                else:
                    right = right - 1
        return res


if __name__ == '__main__':
    nums = [int(num) for num in input().split(' ')]
    s = Solution()
    res = s.threeSum(nums)
    print(res)