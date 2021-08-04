arr = []
searchNum = 0

def binarySearch(l,r):
    global arr
    global searchNum

    size = r-l+1
    
    if size <= 1:
        if arr[l] == searchNum:
             return l
        if arr[r] == searchNum:
            return r
        return False

    mid = size // 2
    mid = mid+l
    
    if arr[mid-1] == searchNum:
        returnNum = mid-1
        return returnNum

    leftC = binarySearch(l, mid-1)
    rightC = binarySearch(mid, r)

    if type(leftC) is int:
        return leftC
    if type(rightC) is int:
        return rightC
    
    return

def runSearch(list, num):
    global arr
    global searchNum

    searchNum = num
    arr = list
    return binarySearch(0, len(list)-1)

print(runSearch([1,6,12,3546,123,6,3,67,12342,235,56], 235))