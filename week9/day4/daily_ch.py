class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    # def set_left(self, value):
    #     # if self.num_of_children < 2:
    #     self.left = Node(value)
    #     # self.num_of_children += 1
    #     print(f"left node created with {self.value}")
    #
    # def set_right(self, value):
    #     # if self.num_of_children < 2:
    #     self.right = Node(value)
    #         # self.num_of_children += 1
    #     print(f"right node created with {self.value}")

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def add_node(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
                print(f"left node created with {self.value}")
            else:
                self.left.add_node(value)

        elif value > self.value:
            if self.right is None:
                self.right = Node(value)
                print(f"right node created with {self.value}")
            else:
                self.right.add_node(value)
        else:
            self.value = value

    def search(self, val):
        if self is None or self.value == val:
            return self
        if val < self.value:
            return self.search(self.right, val)
        if val > self.value:
            return self.search(self.left, val)


# #
# a = Node
# a.add_node(a)


# Insert method to create nodes

# findval method to compare the value with nodes


# Print the tree
#
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print(self.data),
#         if self.right:
#             self.right.PrintTree()


root = Node(27)
root.add_node(15)
root.add_node(14)
root.add_node(35)
root.add_node(31)
root.add_node(10)
root.add_node(19)
# print(root.search(7))
# print(root.search(14))
print(root.search(12))