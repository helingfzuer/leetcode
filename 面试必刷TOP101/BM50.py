#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @param target int整型
# @return int整型一维数组
#
class Solution:
    def twoSum(self, numbers, target: int):
        res = [0]*2
        dic = {}
        for index, num in enumerate(numbers):
            if target - num in dic.keys():
                res[0], res[1] = min(dic[target-num], index+1), max(dic[target-num], index+1)
                break
            else:
                dic[num] = index+1
        return res


if __name__ == '__main__':
    numbers = [int(num) for num in input().split(' ')]
    target = int(input())
    s = Solution()
    res = s.twoSum(numbers, target)
    print(res)
