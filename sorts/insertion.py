numbers = [1325234,234,4538906,1239847,5472,12389,12,235]

def insertionSort(arr, j):
    for x in reversed(range(j)):
        if(arr[j] < arr[x]):
            saveSpot = arr[j]
            arr[j] = arr[x]
            arr[x] = saveSpot
            j = x
    if j == len(numbers)-1:
        return arr
    return(insertionSort(arr, j+1))


    
        
print(insertionSort(numbers, 1))
