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

print(sort([43, 80, 4, 39, 25, 3, 1, 0, 96, 19,234,23,4,234,23,42,534,5,34,23,4,23,4,3,24,234,23,4,235,456,45,645,6,457,54,645,6,456,45,645,6,456,54,65,6,324,123,21,4657,45,6456,45,645,6,546,546,45,654,6,456,45,645,6,456,54,645,623,45,324,234,23,42,4,634,6,34,6]))