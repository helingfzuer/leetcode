while True:
    try:
        s = input()
        res = ''
        for k, v in enumerate(s):
            if '0' <= v <= '9' and (res == '' or res[-1] < '0' or res[-1] > '9'):
                res += '*'
            res += v
            if'0' <= v <= '9' and (k == len(s)-1 or s[k+1] < '0' or s[k+1] > '9'):
                res += '*'
        print(res)
    except:
        break

