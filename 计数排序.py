def countSort(nums):
    if len(nums) <= 1:
        return nums
    dict = {}
    ilist = []
    for i in range(0,11):
        count = 0
        for j in range(len(nums)):
            if nums[j] == i:
                count += 1
                ilist.append(nums[j])
                dict[nums[j]] = count
    return dict,ilist
nums = [2,1,3,0,0,4,2,10,5,6,7,8,4,3,4,6]
print(countSort(nums))

# 官方版计数排序

def countSort1(nums):
    max_value = max(nums)
    count_arr = [0]*(max_value+1)

    for i in range(len(nums)):
        count_arr[nums[i]] += 1

    sort_arr = []
    for i in range(len(count_arr)):
        for j in range(count_arr[i]):
            sort_arr.append(i)
    return sort_arr
if __name__ == '__main__':
    nums = [9,3,5,4,9,1,2,7,8,1,3,6,5,3,4,0,10,9,7,9]
    print(countSort(nums))
