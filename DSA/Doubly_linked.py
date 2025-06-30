class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Dll:
    def __init__(self):
        self.head=None

    def forword_traversal(self):
        if self.head is None:
            print("singly linked list is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next
    def backword_traversal(self):
        print()
        if self.head is None:
            print("double linked list is empty")
        else:
            a=self.head
            while a.next is not None:
                a=a.next
            while a is not None:
                print(a.data,end=" ")
                a=a.prev
    def insertion_at_beginning(self,data):
        print()
        ns= Node(data)
        a=self.head
        a.prev=ns
        ns.next=a
        self.head=ns
    def insertion_at_end(self,data):
        print()
        ne=Node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne
        ne.prev=a
    def insert_at_specified_node(self,position,data):
        print()
        nib= Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        nib.prev=a
        nib.next=a.next
        a.next.prev=nib
        a.next=nib





n1=Node(5)
d11=Dll()
d11.head=n1
n2=Node(10)
n2.prev=n1
n1.next=n2
n3=Node(15)
n3.prev=n2
n2.next=n3
n4=Node(20)
n4.prev=n3
n3.next=n4
d11.forword_traversal()
d11.backword_traversal()
d11.insertion_at_beginning(1)
d11.backword_traversal()
d11.insertion_at_end(13)
d11.forword_traversal()
d11.insert_at_specified_node(4,7)
d11.forword_traversal()

