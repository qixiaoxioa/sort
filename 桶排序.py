from randomList import randomList
nums = randomList.randomList(10)

def boxSort(nums):
    max_c = max(nums)
    min_c = min(nums)
    d = max_c - min_c

    # 初始化桶
    box_num = len(nums)
    count_list = []
    for i in range(box_num):
        count_list.append([])

#     定位元素属于哪个通
    for i in range(len(nums)):
        num = int((nums[i] - min_c)*(box_num - 1)/d)
        bukcet = count_list[num]
        bukcet.append(nums[i])
#     桶内排序
    for i in range(len(count_list)):
        count_list[i].sort()

#   输出
    sort_nums = []
    for sub in count_list:
        for item in sub:
            sort_nums.append(item)
    return sort_nums


print(boxSort(nums))