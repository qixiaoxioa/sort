from typing import List
from randomList import randomList
ilist = randomList.randomList(8)
def merge(left: List,right: List):
    mlist = []
    while left and right:
        if left[0] <= right[0]:
            mlist.append(left.pop(0))
        else:
            mlist.append(right.pop(0))
    if left:
        mlist.extend(left)
    if right:
        mlist.extend(right)
    return mlist

def merge1(left:list,right:list):
    left_len = len(left)
    right_len = len(right)
    mlist = []
    i = 0
    j = 0
    while i < left_len and j < right_len:
        if left[i] < right[j]:
            mlist += [left[i]]
            i += 1
        else:
            mlist+= [right[i]]
            j += 1
    mlist += [left[i:]]
    mlist += [right[j:]]
    return mlist

def mergeSort(nums: List):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left,right = nums[0:mid],nums[mid:]
    return merge1(mergeSort(left),mergeSort(right))

if __name__ == '__main__':
    print(ilist)
    res = mergeSort(ilist)
    print(res)
