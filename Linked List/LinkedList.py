class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        if self.tail is None:
            self(value)
        else:
            node = Node(value)
            self.tail.next = node
            self.tail = self.tail.next
        
        
    

mylist = LinkedList(4)
mylist.append(5)
mylist.append(3)
mylist.append(6)
mylist.print_list()