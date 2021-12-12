while True:
    try:
        n, nums, negCnt, posCnt, posSum = int(input()), [int(num) for num in input().split(' ')], 0, 0, 0
        for num in nums:
            if num > 0:
                posSum += num
                posCnt += 1
            elif num < 0:
                negCnt += 1
        print(negCnt, end=' ')
        if posCnt == 0:
            print('0.0')
        else:
            print(round(posSum/posCnt, 1))
    except:
        break