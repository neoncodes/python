class Heap:
    def __init__(self):
        self.array = [None]*64
        self.nextPos = 0

    def siftUp(self, x):
        if x != 0:
            if self.array[(x-1)//2] > self.array[x]:
                temp = self.array[x]
                self.array[x] = self.array[(x-1)//2]
                self.array[(x-1)//2] = temp
                return self.siftUp((x-1)//2)
            return True
        else:
            return True

    def siftDown(self, x):
        if self.array[2*x+1] and self.array[2*x+2]:
            if self.array[2*x+1] < self.array[2*x+2]:
                temp = self.array[x]
                self.array[x] = self.array[2*x+1]
                self.array[2*x+1] = temp
                return self.siftDown(2*x+1)
            else:
                temp = self.array[x]
                self.array[x] = self.array[2*x+2]
                self.array[2*x+2] = temp
                return self.siftDown(2*x+2)
        elif self.array[2*x+1]:
                temp = self.array[x]
                self.array[x] = self.array[2*x+1]
                self.array[2*x+1] = temp
                return self.siftDown(2*x+1)
        else:
            return True



    def add(self, val):
        self.array[self.nextPos] = val
       

        if self.nextPos != 0:
            self.siftUp(self.nextPos)

        self.nextPos += 1

        return None
    
    def pop(self):
        save = self.array[0]
        self.array[0] = self.array[self.nextPos-1]
        self.array[self.nextPos-1] = None
        self.nextPos -= 1
        self.siftDown(0)
        
        return save


    def print(self):
        return self.array

minHeap = Heap()
minHeap.add(10)
minHeap.add(9)
minHeap.add(8)
minHeap.add(7)
minHeap.add(6)
minHeap.add(5)
minHeap.pop()
print(minHeap.print())