#!/usr/bin/python

class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items ==[] #further conditions implementation needed
        
    
    def enqueue(self, item):
        return self.items.insert(0, item) #further checks needed if queue already contains items
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
        
 
#instantiate the queue object 
q = Queue()

# check the size of the queue
q.size()

#Insert items into the queue

q.enqueue('test1')
q.enqueue('item2')
q.enqueue('Ams')
q.enqueue('CPH')

#check the size again
q.size()

#check if teh queue is empty or not
q.isEmpty()

#delete or dequeue an item
q.dequeue()

#check teh size after the deletion of an item
q.size()
