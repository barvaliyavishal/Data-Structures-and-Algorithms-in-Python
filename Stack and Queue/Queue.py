class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class queue:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
            self.length = 1
        else:
            self.last.next = new_node
            self.last = self.last.next
            self.length += 1

    def dequeue(self):
        if self.length == 0:
            return False
        else:
            temp = self.first
            self.first = temp.next
            temp.next = None
            self.length -= 1
            return temp
        
    
a = queue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.dequeue()
a.dequeue()
a.print_queue()