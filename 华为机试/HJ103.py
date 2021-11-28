import bisect
while True:
    try:
        n, nums = int(input()), [int(num) for num in input().split(' ')]
        d = []
        for num in nums:
            if not d or num >= d[-1]:
                d.append(num)
            else:
                pos = bisect.bisect_left(d, num)
                d[pos] = num
        print(len(d))
    except:
        break