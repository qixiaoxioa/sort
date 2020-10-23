def threeSumClostest(nums:list,target):
    if not nums or len(nums) < 3:
        return None
    if len(nums) == 3:
        return nums[0] + nums[1] + nums[2]
    nums.sort()
    res_ms = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            ans_ms = nums[left] + nums[right] + nums[i]
            if abs(ans_ms-target) < abs(res_ms-target):
                res_ms = ans_ms
            if ans_ms > target:
                right -= 1
            elif ans_ms < target:
                left += 1
            else:
                return target
    return res_ms
nums = [-1,0,1,-9]
print(threeSumClostest(nums,100))

