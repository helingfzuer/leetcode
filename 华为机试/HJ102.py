while True:
    try:
        s = input()
        dic = {}
        for char in s:
            if char not in dic.keys():
                dic[char] = 1
            else:
                dic[char] += 1
        dic = sorted(dic.items(), key=lambda x: x[0])
        dic = sorted(dic, key=lambda x: x[1], reverse=True)
        print(''.join(k for (k, v) in dic))
    except:
        break
