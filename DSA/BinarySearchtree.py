# Creation of a node
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

# Inorder traversal function
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + " ->", end=' ')
        inorder(root.right)

# Insert a node to the tree
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Delete a node from the tree
def deleteNode(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)

    return root

# Find minimum value node
def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Constructing the BST
root = None
root = insert(root, 9)
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 7)
root = insert(root, 8)
root = insert(root, 11)
root = insert(root, 15)
root = insert(root, 5)

print("Inorder traversal: ", end='')
inorder(root)

print("\n\nDelete 11")
root = deleteNode(root, 11)

print("Inorder traversal: ", end='')
inorder(root)