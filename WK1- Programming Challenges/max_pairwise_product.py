#Uses python3

def max_prod(nums):
	n = len(nums)
	max_num1 = n-1
	max_num2= n-1

	for i in range(n):
		if(nums[i]>nums[max_num1]):
			max_num1 = i
	for j in range(n):
		if (j!= max_num1 and ( nums[j]> nums[max_num2])) or (max_num2 == max_num1):
			max_num2 = j

	return ((nums[max_num1])) * nums[max_num2]

if __name__ == '__main__':
	input_n = int(input())
	input_nums = [int(x) for x in input().split()]
	print(max_prod(input_nums))


