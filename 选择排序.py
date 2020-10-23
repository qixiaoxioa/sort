from randomList import randomList
llist = randomList.randomList(20)
def select(nums:list):
    if len(nums) <= 1:
        return nums
    for i in range(len(nums)-1): #外层循环空值多少轮
        minlist = i
        for j in range (i + 1,len(nums)):#内层循环负责找到最小值索引
            if nums[minlist] > nums[j]:
                minlist = j
        nums[i],nums[minlist] = nums[minlist],nums[i]
        print(f"第{i}轮排序结果", end="")
        print(nums)
    return nums
if __name__ == '__main__':
    print("原始数据:",llist)
    select(llist)
