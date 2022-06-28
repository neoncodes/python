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

print(sort([43, 80, 4, 39, 25, 3, 1, 0, 96, 19,234,23,4,234,23,42,534,5,34,23,4,23,4,3,24,234,23,4,235,456,45,645,6,457,54,645,6,456,45,645,6,456,54,65,6,324,123,21,4657,45,6456,45,645,6,546,546,45,654,6,456,45,645,6,456,54,645,623,45,324,234,23,42,4,634,6,34,6]))