class Solution:
    def lengthOfLIS(self, nums) -> int:
        d = []
        for num in nums:
            if not d or num > d[-1]:
                d.append(num)
            else:
                left, right = 0, len(d)-1
                pos = right
                while left <= right:
                    mid = (left+right) // 2
                    if d[mid] >= num:
                        pos = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                d[pos] = num
        return len(d)


if __name__ == '__main__':
    n = int(input())
    nums = [int(num) for num in input().split(' ')]
    s = Solution()
    res = s.lengthOfLIS(nums)
    print(res)