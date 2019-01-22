#!/usr/bin/python

class stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        if item not in self.items:
            self.items.append(item) #other operations could be used of the list
            return True
        return False
    
    def pop(self):
        if len(self.items) <=0:
            return "stack is empty:"
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
        
#Initaite an object
s = stack()

#check if the stack is empty
print(s.isEmpty())

#add an element to the stack s
s.push(6)

#check if the stack is not empty
print(s.isEmpty())

# add more items
s.push("Abbott")
s.push("End")
s.push("IT")

#check teh size of the stack
s.size()

#remove the top element, Keep in mind that stack works in a LIFO (Last in First out) fashion
s.pop()

#top element fo teh stack
s.peek()

#check to enter a duplicate element
s.push(6) #entering a duplicate item, rejected by stack


