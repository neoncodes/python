array = []
pos = 0

def fib(n, x, max):
    global array
    global pos
    if array == []:
        array = [None]*max
        
        array[pos] = x
        array[pos+1] = n
        pos += 2
    if n > max:
        return array
    array[pos] = n+x
    pos += 1
    return fib(n+x, n, max)
    
print(fib(1, 0, 10000))

# implementation of the fibonaci 