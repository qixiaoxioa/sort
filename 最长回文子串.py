def centerSpread(strs, left:int, right:int):
    i = left
    j = right
    length = len(strs)
    while i >= 0 and j <length:
        if strs[i] == strs[j]:
            i -= 1
            j += 1
        else:
            break
    return strs[i+1:j]


def longestpalindrome(strs:str):
    length = len(strs)
    if length < 2:
        return strs
    maxlen = 1
    res = strs[0]
    for i in range(length - 1 ):
        odd = centerSpread(strs,i,i)
        even = centerSpread(strs,i,i + 1)
        maxstr = odd if len(odd) > len(even) else even
        if len(maxstr) > maxlen:
            maxlen = len(maxstr)
            res = maxstr
    return res,maxlen
if __name__ == '__main__':
    strs = '132011100101001110231'
    print(longestpalindrome(strs))