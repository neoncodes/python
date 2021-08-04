def merge(left, right):
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

def sort(arr):

    size = len(arr)

    if size == 1:
        return arr
    
    mid = size // 2
    left = arr[mid:]
    right = arr[:mid]
    
    return merge(sort(left), sort(right))

    # return merge(left, right)

print(sort([2123465,1235,12346325,23451345,123451235,34263467,23465547,45373547,34572462345,23464575878,4252348523758732462346,245745376357246]))