from randomList import randomList
llist = randomList.randomList(20)
def bubble(nums:list):
    if len(nums) <= 1:
        return nums
    for i in range(1,len(nums)):
        flag = True
        for j in range(len(nums)-i):
            if nums[j] > nums[j + 1]:
                nums[j],nums[j +1] = nums[j + 1],nums[j]
                flag = False
        if flag:
            break
        print(f"第{i}轮排序结果",end="")
        print(nums)
    return nums
if __name__ == '__main__':
    print("原始数据:",llist)
    bubble(llist)