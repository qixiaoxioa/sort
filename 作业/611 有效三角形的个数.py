def sanjiaoSum(nums:list):
    nums.sort()
    count = 0
    for i in range(2,len(nums)):
        left = 0
        right = i - 1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                count += right - left
                right -= 1
            else:
                left += 1
    return count
nums = [1,3,5,7,10]
print(sanjiaoSum(nums))