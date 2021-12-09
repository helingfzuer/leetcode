while True:
	try:
		n, nums, k = int(input()), [int(num) for num in input().split(' ')], int(input())
		flag = True if k == 1 else False
		nums = [str(num) for num in sorted(nums, reverse=flag)]
		print(' '.join(nums))
	except:
		break
