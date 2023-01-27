class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        return True


    def pop(self):
        if self.length == 0:
            return None

        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp


    def prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length += 1
        return True

    
    def print_list(self):
        if self.length == 0:
            print("List is Empty")
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next
        print("Length : " ,self.length)


    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if self.length == 0 or index < 0 or index >= self.length:
            return None
        if index < int(self.length/2):
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range((self.length-index)-1):
                temp = temp.prev
        return temp
    
    def set(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
        return node

    def insert1(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.add_first(value)
            return True
        elif index == self.length:
            self.prepend(value)
            return True
        node = Node(value)
        before = self.get(index-1)
        after = before.next
        node.next = after
        node.prev = before
        after.prev = node
        before.next = node
        self.length += 1

    def remove(self, index):
        if index < 0  or index >= self.length:
            return None
        elif index == 0:
            self.pop_first()
        elif index == self.length-1:
            self.pop()
        else:
            temp = self.get(index-1)
            temp.next.next.prev = temp
            temp.next = temp.next.next
            self.length -= 1

    def print_reverse(self):
        temp = self.tail
        while temp:
            print(temp.value)
            temp = temp.prev


mylist = DoublyLinkedList(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.append(6)
mylist.append(7)
mylist.append(8)
mylist.append(9)
mylist.append(10)
mylist.insert1(7,10)
mylist.remove(7)
mylist.insert1(3,10)
mylist.print_list()
