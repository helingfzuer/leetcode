# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def initList(nums):
    head = ListNode(nums[0])
    p = head
    for num in nums[1:]:
        tmpNode = ListNode(num)
        p.next = tmpNode
        p = p.next
    return head


class Solution:
    def reversePrint(self, head: ListNode):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]


if __name__ == '__main__':
    nums = [int(num) for num in input().split(' ')]
    l = initList(nums)
    s = Solution()
    res = s.reversePrint(l)
    print(res)