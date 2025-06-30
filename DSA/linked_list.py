# creating a node

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Sll:
    def __init__(self):
        self.head=None

    def traversal(self):
        if self.head is None:
            print("singly linked list is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next
    def insert_at_beginning(self,data):
        print()
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_at_end(self,data):
        print()
        ne=Node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne
    def insert_at_specified_node(self,position,data):
        print()
        nib= Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        nib.next=a.next
        a.next=nib

    def deletion_at_beginning(self):
        print()
        a=self.head
        self.head=a.next
        a.next=None



    def deletion_at_end(self):
        print()
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            # Only one node
            self.head = None
            return

        a = self.head
        while a.next.next is not None:
            a = a.next
        a.next = None

    def deletion_at_particular_nade(self, position):
        print()
        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            temp = self.head
            self.head = temp.next
            temp.next = None
            return

        a = self.head
        for i in range(1, position - 1):
            if a.next is None:
                print("Invalid position")
                return
            a = a.next

        temp = a.next
        if temp is None:
            print("Invalid position")
            return

        a.next = temp.next
        temp.next = None


n1=Node(5)
s11=Sll()
s11.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
n4=Node(20)
n3.next=n4
s11.traversal()
s11.insert_at_beginning(2)
s11.traversal()
s11.insert_at_specified_node(3,5)
s11.traversal()
s11.deletion_at_beginning()
s11.traversal()
s11.deletion_at_end()
s11.traversal()
s11.deletion_at_particular_nade(3)
s11.traversal()






