def merge(arr):      
    size = len(arr)
    mid = size // 2

    left = arr[:mid]
    right = arr[mid:]

    if size == 1:
        return arr

    arr = []


    check = True

    while check:
        if not left or not right:
            if left:
                for x in left:
                    arr.append(x)
            if right:
                for x in right:
                    arr.append(x)
            check = False
        else:
            if left[0] > right[0]:
                arr.append(right[0])
                right.pop(0)
            else:
                arr.append(left[0])
                left.pop(0)

    return arr
    
array = [1325234,234,4538906,1239847,5472,12389,12,235]

def sort(l, r):

    size = r

    if(l == r):
        return False

    mid = size // 2

    sort(0, mid)
    sort(mid, size-1)

    return merge(array)
print(sort(0,len(array)-1))
print(merge(array))