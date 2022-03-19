#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return int整型
#
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        res, cnt = numbers[0], 1
        for num in numbers[1:]:
            if cnt == 0:
                res, cnt = num, 1
            else:
                cnt = cnt + 1 if num == res else cnt - 1
        return res


if __name__ == '__main__':
    numbers = [int(num) for num in input().split(' ')]
    s = Solution()
    res = s.MoreThanHalfNum_Solution(numbers)
    print(res)