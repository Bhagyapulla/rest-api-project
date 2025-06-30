# print(end="Enter the size of Array: ")
# tot = int(input())
# arr = []  # Initialize the list before using it
# print(end="Enter " + str(tot) + " Elements: ")
# for i in range(tot):
#     arr.append(input())
# print(end="\nEnter the value to Delete:")
# val = input()
# if val in arr:
#     arr.remove(val)
#
#
# stack=[]
# stack.append("welcome")
# stack.append("to")
# stack.append("DSA")
# print(stack)
# print(stack.pop())
# print(stack)

# from _collections import deque
#
# stack=deque()
# stack.append("bhagya")
# stack.append("enay")
# print(stack.pop())
# print(stack)
#
# from  queue import LifoQueue
#
# stack=LifoQueue(maxsize=3)
# stack.put(2)
# stack.put(3)
# stack.put(4)
# print(stack)
# print(stack.qsize())
# print(stack.full())
# stack.get()
# print(stack.full())
#
class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue)<1:
            return None
        return self.queue.pop(0)
    def display(self):
        print(self.queue)
    def size(self):
        return len(self.queue)

q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.display()
q.dequeue()
print("after removing an element")
q.display()

