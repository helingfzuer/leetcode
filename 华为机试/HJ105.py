if __name__ == '__main__':
    count_total, count_neg, sum_notNeg = 0, 0, 0
    while True:
        try:
            num = int(input())
            count_total += 1
            if num < 0:
                count_neg += 1
            else:
                sum_notNeg += num
        except:
            break
    print(count_neg)
    res = 0 if sum_notNeg == 0 else sum_notNeg/(count_total-count_neg)
    print(format(res, '.1f'))



