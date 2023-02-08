class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class stack:
    def __init__(self,value) -> None:
            new_node = Node(value)
            self.top = new_node
            self.height = 1
    

    def print_stack(self):
        temp = self.top 
        while temp:
             print(temp.value)
             temp = temp.next


    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1
    

    def pop(self):
        if self.height == 0:
            return False
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1


a = stack(4)
a.pop()
a.pop()
a.push(1)
a.print_stack()
print("***********")
a.push(5)
a.push(6)
a.push(7)
a.print_stack()
print("after delete")
a.pop()
a.print_stack()