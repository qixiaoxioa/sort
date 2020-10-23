
def swap(array,a,b):
    array[a],array[b] = array[b],array[a]

def partition(ilist,start,end):
    pivot = ilist[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and ilist(p) < pivot:
            p += 1
        while p <= q and ilist(q) >= pivot:
            q -= 1
        if p < q:
            swap(ilist,p,q)
    swap(ilist,start,q)
    return q

#  快慢指针法
def partition1(ilist,start,end):
    pivot = ilist[start]
    mask = start
    for i in range (start + 1, end + 1):
        if ilist[i] < pivot:
            mask += 1
            ilist[i], ilist[mask] = ilist[mask], ilist[i]
            # swap(ilist,i,mask)
    ilist[start] = ilist[mask]
    ilist[mask] = pivot
    return mask




def quickSort(ilist,start,end):
    if start >= end:
        return
    mid = partition1(ilist,start,end)
    quickSort(ilist,start,mid-1)
    quickSort(ilist,mid + 1,end)

if __name__ == '__main__':

   ilist = [7,1,2,5,4,8,5]
   print(ilist)
   quickSort(ilist,0,len(ilist) - 1)
   print(ilist)