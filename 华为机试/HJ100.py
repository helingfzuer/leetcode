while True:
    try:
        n = int(input())
        res = 2*n + 3*n*(n-1)//2
        print(res)
    except:
        break