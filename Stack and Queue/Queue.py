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
    
a = queue(1)
a.print_queue()