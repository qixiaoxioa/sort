def minSubArrayLen1(s:int,nums:list):
    left,sums,res = 0,0,float('inf')
    for right in range(len(nums)):
        sums += nums[right]
        while sums >= s:
            if right-left+1 < res:
                res = right - left + 1
            sums -= nums[left]
            left += 1
    return 0 if res == float('inf') else res
nums = [2,3,2,4,3]
print(minSubArrayLen1(7,nums))



