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
        return True
    

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
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self,index):
        if self.head is None:
            return None
        elif index >= self.length or index < 0:
            return "Index out of bound"

        temp = self.head
        while index > 0:
            temp = temp.next
            index -= 1
        
        return temp
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None

        new_node = Node(value)
        temp = self.head

        if index == 0:
            new_node.next = temp
            self.head = new_node

        elif index == self.length:
            self.tail.next = new_node
            self.tail = self.tail.next

        else:
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1

    def set_value(self, index, value):
        if index < 0 or index >= self.length or self.length == 0:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return True

    def set_value2(self, index, value):
        ans = self.get(index)
        if type(ans) == Node:
            ans.value = value
            return True
        return False
    
    def remove(self, index):
        if index < 0  or index >= self.length:
            return None

        temp = self.head
        if index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        
        for _ in range(index-1):
            temp = temp.next
        if temp.next:
            node = temp.next
            temp.next = node.next
            node.next = None
            return node

        


mylist = LinkedList(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.print_list()
mylist.remove(0)
print("\n\nAfter")
mylist.print_list()

 