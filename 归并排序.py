from randomList import randomList
from typing import List
ilist = randomList.randomList(20)


def merge(left: List, right: List):
    new_list = []
    while left and right:
        if left[0] > right[0]:
            new_list.append(right.pop(0))
        else:
            new_list.append(left.pop(0))
    if left:
        new_list.extend(left)
    if right:
        new_list.extend(right)
    return new_list

def merge1(left, right):
    left_len = len(left)
    right_len = len(right)
    mlist = []
    i = 0
    j = 0
    while i < left_len and j < right_len:
        if left[i] < right[j]:
            mlist.append(left[i])
            i += 1
        else:
            mlist.append(right[j])
            j += 1
    mlist.extend(left[i:])
    mlist.extend(right[j:])
    return mlist

def mergerSort(nums: List):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left,right = nums[0:mid],nums[mid:]
    return merge(mergerSort(left),mergerSort(right))

if __name__ == '__main__':
    print(ilist)
    print(mergerSort(ilist))
