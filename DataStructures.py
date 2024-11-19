# --- Array Implementation ---
class Array:
    def __init__(self):
        self.data = []
    
    def insert(self, value):
        self.data.append(value)
    
    def delete(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]
    
    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        return None

# --- Stack Implementation ---
class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, value):
        self.data.append(value)
    
    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        return None
    
    def is_empty(self):
        return len(self.data) == 0

# --- Queue Implementation ---
class Queue:
    def __init__(self):
        self.data = []
    
    def enqueue(self, value):
        self.data.append(value)
    
    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.data[0]
        return None
    
    def is_empty(self):
        return len(self.data) == 0

# --- Singly Linked List Implementation ---
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def delete(self, value):
        current = self.head
        if current and current.data == value:
            self.head = current.next
            return
        while current and current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
    
    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# --- Rooted Tree Implementation ---
class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)
    
    def remove_child(self, child_node):
        self.children.remove(child_node)

# --- Example Usage and Output ---
# Array Example
array = Array()
array.insert(10)
array.insert(20)
array.insert(30)
array.delete(1)
print("Array after insertions and deletion:", array.data)

# Stack Example
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack after pushes:", stack.data)
stack.pop()
print("Stack after pop:", stack.data)
print("Stack peek:", stack.peek())

# Queue Example
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Queue after enqueue:", queue.data)
queue.dequeue()
print("Queue after dequeue:", queue.data)
print("Queue peek:", queue.peek())

# Linked List Example
linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
print("Linked List after insertions:", linked_list.traverse())
linked_list.delete(20)
print("Linked List after deletion:", linked_list.traverse())

# Rooted Tree Example
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
root.add_child(child1)
root.add_child(child2)
print("Rooted Tree structure:")
print("Root:", root.data)
for child in root.children:
    print("Child node:", child.data)
