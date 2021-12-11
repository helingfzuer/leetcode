class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = a ^ b, (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)


if __name__ == '__main__':
    a, b = int(input()), int(input())
    s = Solution()
    res = s.add(a, b)
    print(res)