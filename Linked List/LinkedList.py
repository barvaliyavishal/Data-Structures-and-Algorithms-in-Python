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
        print("length is : ", self.length)

    def append(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.length = 1
        else:
            
            self.tail.next = node
            self.tail = node
            self.length += 1
    

    def pop(self):
        if self.head is None:
            return 
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        

mylist = LinkedList(4)
mylist.append(5)
mylist.append(3)
mylist.append(6)
mylist.pop()
mylist.append(6)
print("complete List \n")
mylist.print_list()
print("\n Head is : ",mylist.head.value)
print("\n Tail is : ",mylist.tail.value)
