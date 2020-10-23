from randomList import randomList
ilist = randomList.randomList(20)

def swap(nums:list,a,b):
    nums[a],nums[b]= nums[b],nums[a]


def partition(ilist,start,end):
    povio = ilist[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and ilist[p] < povio:
            p += 1
        while p <= q and ilist[q] >= povio:
            q -= 1
        if p < q:
            swap(ilist,p,q)
    swap(ilist,start,q)
    return q

def quickSort(ilist, start, end):
    if start >= end :
        return
    mid = partition(ilist,start,end)
    quickSort(ilist, start, mid - 1)
    quickSort(ilist, mid + 1, end)

if __name__ == '__main__':
    print(ilist)
    quickSort(ilist, 0, len(ilist) - 1)
    print(ilist)