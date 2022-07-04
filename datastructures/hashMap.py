from datastructures.linkedList import LinkedList


class HashMap:
    def __init__(self):
        self.keyList = [LinkedList()] * 1
        self.itemList = [LinkedList()] * 1

    def set(self, key, item):
        i = hash(key) % len(self.keyList)
        x = 0
        cont = False
        temp = self.keyList[i].head
        if temp:
            if temp.value == key:
                self.itemList[i].head.value = item
                return True
            while temp.nextNode:
                if temp.nextNode.value == key:
                    cont = True
                elif temp.nextNode.nextNode:
                    temp = temp.nextNode
                    x += 1
                else:
                    break

            if cont:
                temp = self.itemList[i].head
                for _ in range(0, x):
                    temp = temp.nextNode
                temp.value = item
                return True

        self.keyList[i].append(key)
        self.itemList[i].append(item)

    def delete(self, key):
        i = hash(key) % len(self.keyList)
        x = self.keyList[i].remove(key)
        temp = self.itemList[i].head
        save = None
        z = 0
        for z in range(0, z):
            if z > 0:
                save = temp
            temp = temp.nextNode
        if z < 1:
            temp.head = None
            return False
        if temp.nextNode:
            save.nextNode = save.nextNode.nextNode
        else:
            save.nextNode = None

    def get(self, key):
        i = hash(key) % len(self.keyList)
        temp = self.keyList[i].head
        x = 0
        while temp:
            if temp.value == key:
                break
            elif temp.nextNode:
                temp = temp.nextNode
                x += 1
            else:
                raise Exception(f"Cannot find '{key}' in HashMap!")

        temp = self.itemList[i].head
        for _ in range(0, x):
            temp = temp.nextNode
        return temp.value

    def __repr__(self):
        array = []
        for x, y in zip(self.keyList, self.itemList):
            if not x.head.nextNode and not y.head.nextNode:
                array.append(f"{x.head.value}:{y.head.value}")
            else:
                x = x.head
                y = y.head
                while x.nextNode:
                    array.append(f"{x.value}:{y.value}")
                    x = x.nextNode
                    y = y.nextNode
                array.append(f"{x.value}:{y.value}")
        return str(array)


m = HashMap()
m.set("charley", "wolf")
m.set("charley", "yoyasdfu")
m.set("charley", "hi")
m.set("adfh", "adtgfg")
m.set("dfhgj", "dfdf")
m.set("werwer", "werewr")
m.delete("werwer")
print(m)
