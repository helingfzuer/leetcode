class Solution:
    def replaceSpace(self, s) -> str:
        return s.replace(' ', '%20')


if __name__ == '__main__':
    strs = input()
    s = Solution()
    res = s.replaceSpace(strs)
    print(res)