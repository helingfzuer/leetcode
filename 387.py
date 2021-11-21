class Solution:
    def firstUniqChar(self, s: str) -> int:
        pos = {}
        for i, ch in enumerate(s):
            if ch in pos.keys():
                pos[ch] = -1
            else:
                pos[ch] = i
        res = len(s)
        for position in pos.values():
            if position != -1 and position < res:
                res = position
        return -1 if res == len(s) else res


if __name__ == '__main__':
    strs = input()
    s = Solution()
    res = s.firstUniqChar(strs)
    print(res)