class Solution:
    def majorityElement(self, nums) -> int:
        cnt, res = 0, -1
        for num in nums:
            if cnt == 0:
                res, cnt = num, 1
            else:
                cnt = cnt + 1 if res == num else cnt - 1
        return res if nums.count(res) > len(nums) // 2 else -1


if __name__ == '__main__':
    nums = [int(num) for num in input().split(' ')]
    s = Solution()
    res = s.majorityElement(nums)
    print(res)