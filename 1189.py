import collections
from typing import Collection


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = collections.Counter(text)
        return min(dic['b'], dic['a'], dic['l'] // 2, dic['o'] // 2, dic['n'])


if __name__ == '__main__':
    text = input()
    s = Solution()
    res = s.maxNumberOfBalloons(text)
    print(res)
