def removeZero(nums:list):
    fast = 0
    slow = 0
    while fast < len(nums):
        if nums[fast] == 0:
            fast += 1
        else:
            nums[slow] = nums[fast]
            fast += 1
            slow += 1
    for i in range(slow,len(nums)):
        nums[i] = 0
    return nums
nums = [2,1,3,0,0,4,2]
print(removeZero(nums))

# 去重





