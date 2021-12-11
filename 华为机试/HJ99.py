while True:
    try:
        n, res = int(input()), 0
        for num in range(0, n+1):
            if num == 0 or num%10 == 1 or num%10 == 5 or num%10 == 6:
                if str(num**2).endswith(str(num)):
                    res += 1
        print(res)
    except:
        break