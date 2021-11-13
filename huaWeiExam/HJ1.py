if __name__ == '__main__':
	s = input()
	res = 0
	for char in s[: : -1]:
		if char == ' ':
			break
		else:
			res += 1
	print(res)
