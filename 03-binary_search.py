def binarysearch(target, nums):
	floor_index = -1
	ceil_index = len(nums)

	while floor_index + 1 < ceil_index:
		guess_index = floor_index +  (ceil_index-floor_index)//2
		guess_value = nums[guess_index]

		if guess_value == target:
			return True
		if guess_value > target:
			ceil_index = guess_index
		if guess_value < target:
			floor_index = guess_index
	return False
