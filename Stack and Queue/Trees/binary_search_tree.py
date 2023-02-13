class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        temp = self.root
        if temp is None:
            self.root = new_node
            return True
        else:
            while True:
                if temp.value == value:
                    return False
                if temp.value < value:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right
                else:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left

    def contains(self, value):
        temp = self.root

        while temp:
            if temp.value == value:
                return True
            if temp.value < value:
                temp = temp.right
            else:
                temp = temp.left
        return False
                




my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.contains(27))
print(my_tree.contains(17))

