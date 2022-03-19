#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def FindNumsAppearOnce(self, array):
        tmp, mask = 0, 1
        for num in array:
            tmp ^= num
        while tmp & mask == 0:
            mask <<= 1
        res = [0]*2
        for num in array:
            if num & mask == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        res[0], res[1] = min(res[0], res[1]), max(res[1], res[0])
        return res


if __name__ == '__main__':
    nums = [int(num) for num in input().split(' ')]
    s = Solution()
    res = s.FindNumsAppearOnce(nums)
    print(res)