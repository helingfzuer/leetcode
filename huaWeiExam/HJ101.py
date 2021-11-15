if __name__ == '__main__':
	while True:
		try:
			n = input()
			nums = [int(x) for x in input().split(' ')]
			flag = False if input() == '0' else True
			res = [str(num) for num in sorted(nums, reverse=flag)]
			print(' '.join(res))
		except:
			break