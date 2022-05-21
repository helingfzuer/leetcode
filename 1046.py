import heapq


class Solution:
    def lastStoneWeight(self, stones) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x, y = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            if x != y:
                heapq.heappush(maxHeap, x-y)
        return -maxHeap[0] if maxHeap else 0


if __name__ == '__main__':
    stones = [int(stone) for stone in input().split(' ')]
    s = Solution()
    res = s.lastStoneWeight(stones)
    print(res)