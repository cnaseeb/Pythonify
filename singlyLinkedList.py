#!/usr/bin/python

"""Implements the LinkedList in Python"""

"""LinkedList: example demonstration
    node1 = Node(23)
    node2 = Node(56)
    node3 = Node(51)
    node1.next = node2
    node2.next = node3 """
   
 #Implement a Link list in Python
class Node:      
    def __init__(self, val):
        self.val = val
        self.next = None
        return
    
   
    
class singlyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        return
    
    def size(self):
        currentNode = self.head
        count = 0
        while currentNode is not None:
            count += 1
            currentNode = currentNode.next
        return count
    
    def printNodes(self):
        currentNode = self.head
        
        while currentNode is not None:
            print(currentNode.val)
            currentNode = currentNode.next
        return
    
    def addNodes(self, node):
        if not isinstance(node, Node):
            node = Node(node)
            
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            
        self.tail = node
        
        return
        
node1 = Node(23)
node2 = Node(56)
node3 = Node(51)

for currentNode in [node1, node2, node3]:
    myList.addNodes(currentNode)
    print(myList.size)
    myList.printNodes()
