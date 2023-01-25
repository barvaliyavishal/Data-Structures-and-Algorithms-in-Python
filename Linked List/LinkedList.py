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
        if self.head is None:
            print("List is Empty")
            return 
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
            self.length += 1
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1
    

    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            pre = self.head
            while temp.next:
                pre = temp
                temp = temp.next
               
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp.value


    def prepend(self, value):
        new_node = Node(value= value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        

mylist = LinkedList(4)
mylist.append(7)
mylist.append(6)
print("complete List \n")
print("Before Prepand")
mylist.print_list()
mylist.prepend(1)
print("\n\n After Prepand \n")
mylist.print_list()