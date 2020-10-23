# 冒泡排序
from randomList import randomList
llist = randomList.randomList(20)
def bubble(nums:list):
    if len(nums) <= 1:
        return nums
    for i in range(1,len(nums)):
        for j in range(len(nums)-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
        print(nums)
    return nums

def select(nums:list):
    if len(nums) <= 1:
        return nums
    for i in range(len(nums) - 1):
        minlist = i
        for j in range(i+1,len(nums)):
            if nums[minlist]> nums[j]:
                minlist = j
        nums[minlist],nums[i] = nums[i],nums[minlist]
        print(nums)
    return nums
if __name__ == '__main__':
    # print(bubble(llist))
    print(select(llist))