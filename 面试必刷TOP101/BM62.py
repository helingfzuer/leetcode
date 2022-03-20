#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
def multiply(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            c[i][j] = (a[i][0]*b[0][j] + a[i][1]*b[1][j])
    return c


def matrixPow(a, n):
    res = [[1, 0], [0, 1]]
    while n > 0:
        if n & 1:
            res = multiply(res, a)
        n >>= 1
        a = multiply(a, a)
    return res


class Solution:
    def Fibonacci(self, n) -> int:
        if n <= 2:
            return 1
        res = matrixPow([[1, 1], [1, 0]], n-1)
        return res[0][0]


if __name__ == '__main__':
    n = int(input())
    s = Solution()
    res = s.Fibonacci(n)
    print(res)