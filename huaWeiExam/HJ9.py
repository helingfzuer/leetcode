if __name__ == '__main__':
	n = input()
	res = ''
	for num in n[: : -1]:
		if num not in res:
			res += num
	print(res)