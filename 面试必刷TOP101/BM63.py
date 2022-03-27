#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param number int整型
# @return int整型
#
class Solution:
    def jumpFloor(self, number: int) -> int:
        if number <= 2:
            return number
        f1, f2 = 1, 2
        for i in range(3, number+1):
            f1, f2 = f2, f1+f2
        return f2


if __name__ == '__main__':
    num = int(input())
    s = Solution()
    res = s.jumpFloor(num)
    print(res)