class Solution:
    def repeatedNTimes(self, nums) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i % n] == nums[(i+1) % n] or nums[i % n] == nums[(i+2) % n]:
                return nums[i % n]
            i += 1
        return -1


if __name__ == '__main__':
    nums = [int(num) for num in input().split(' ')]
    s = Solution()
    res = s.repeatedNTimes(nums)
    print(res)