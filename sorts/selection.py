numbers = [1325234,234,4538906,1239847,5472,12389,12,235]

newArray = []

def selectionSort(arr):
    if arr == []:
        return True
    
    newLow = arr[0]

    for x in arr:
        if x < newLow:
            newLow = x
    
    newArray.append(newLow)
    arr.remove(newLow)
    print(newLow)
    return selectionSort(arr)

selectionSort(numbers)
print(newArray)
    