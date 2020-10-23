def insert(ilist:list):
    if len(ilist) <= 1:
        return ilist
    for i in range(1,len(ilist)):
        right = ilist[i]
        for j in range(i):
            if ilist[j] > right:
                ilist[j+1:i+1] = ilist[j:i]
                ilist[j] = right
                break
        print(f"第{i}轮排序结束",end="")
        print(ilist)
    return ilist

if __name__ == '__main__':

    ilist = [5,8,6,3,9,2,1,7]
    print(insert(ilist))
