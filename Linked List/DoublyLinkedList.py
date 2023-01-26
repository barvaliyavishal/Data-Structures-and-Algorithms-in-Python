class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
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
            self.length = 1
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = node
            node.prev = temp
            self.tail = node
            self.length += 1


    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1

        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1


    def add_first(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            self.length += 1

    
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
        else:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1

    def get(self, index):
        if self.length == 0 or index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self, index, value):
        if self.length == 0 or index < 0 or index >= self.length:
            return None
        node = self.get(index)
        node.value = value
        return True


    def insert(self, index,value):
        if index < 0 or index > self.length:
            return None

        temp = self.head

        if index == 0:
            self.add_first(value)
            return True

        elif index == self.length:
            self.append(value)
            return True

        node = Node(value)
        for _ in range(index-1):
            temp = temp.next
        node.next = temp.next
        node.prev = temp
        temp.next.prev = node
        temp.next = node
        self.length += 1

        return True

    def remove(self, index):
        if index < 0  or index >= self.length:
            return None
        elif index == 0:
            self.pop_first()
        elif index == self.length-1:
            self.pop()
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            temp.next.next.prev = temp
            temp.next = temp.next.next
            self.length -= 1

        


mylist = LinkedList(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)

mylist.remove(3)
mylist.print_list()