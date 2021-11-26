if __name__ == '__main__':
    num = float(input())
    res = num
    while abs(res**3-num) > 1e-3:
        res = res - (res**3-num)*1.0 / (3*res*res)
    print(format(res, '.1f'))