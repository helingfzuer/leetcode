class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


if __name__ == '__main__':
    matrix = []
    m = int(input())
    for i in range(m):
        matrix.append([int(num) for num in input().split(' ')])
    target = int(input())
    s = Solution()
    res = s.findNumberIn2DArray(matrix, target)
    print(res)