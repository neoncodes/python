def partition(list):
    size = len(list)

    p = size-1
    j = 0
    i = -1

    while j < p:
        if list[j] < list[p]:
            i = i+1
            saveSpot = list[i]
            list[i] = list[j]
            list[j] = saveSpot 
        j += 1

    saveVar = list[i+1]
    list[i+1] = list[p]
    list[p] = saveVar

    return [list,i+1]

def sort(list):
    # recursively sort subarrays (left & right)
    # combine by doing nothing and return sorted

    size = len(list)

    if size <= 1:
        return list

    parter = partition(list)
    list = parter[0]

    mid = parter[1]
    left = list[:mid]
    right = list[mid:]

    return(sort(left)+sort(right))

print(sort([43, 80, 4, 39, 25, 3, 1, 0, 96, 19]))