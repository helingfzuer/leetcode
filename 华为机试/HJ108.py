def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m%n)

if __name__ == '__main__':
    nums = [int(num) for num in input().split(' ')]
    m, n = nums[0], nums[1]
    res = m*n // gcd(m, n)
    print(res)
