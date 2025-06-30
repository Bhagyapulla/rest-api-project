class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

    def traPreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traPreOrder()
        if self.right:
            self.right.traPreOrder()

    def traInOrder(self):
        if self.left:
            self.left.traInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traInOrder()

    def traPostOrder(self):
        if self.left:
            self.left.traPostOrder()
        if self.right:
            self.right.traPostOrder()
        print(self.val, end=' ')


# Create nodes and form the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

# Traversal outputs
print("Pre order Traversal:", end=' ')
root.traPreOrder()

print("\nIn order Traversal:", end=' ')
root.traInOrder()

print("\nPost order Traversal:", end=' ')
root.traPostOrder()