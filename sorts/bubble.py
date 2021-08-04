numbers = [1325234,234,4538906,1239847,5472,12389,12,235]

def bubbleSort(arr):
    num = 0
    check = False

    for num in range(len(numbers)-1):
        if arr[num] > arr[num+1]:
            saveSpot = arr[num]
            arr[num] = arr[num+1]
            arr[num+1] = saveSpot
            check = True
    if check == True:
        return bubbleSort(arr)
    return arr
        
print(bubbleSort(numbers))
