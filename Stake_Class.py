class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class Stack_LL:
    def __init__(self):
        self.top = None
        self.n = 0
        
    def __str__(self):
        result = ""
        current = self.top
        
        while current != None:
            
            result = result + f"{current.data}" + "\n"
            current = current.next
        
        return result
        
    def isempty(self):
        return self.top == None
    
    def push(self,value):
        New = Node(value)
        
        New.next = self.top
        
        self.top = New
        
        self.n = self.n + 1
        
    def peak(self):
        
        if self.isempty() == True:
            return "Stack is Empty"
        return self.top.data
    
    def pop(self):
        
        if self.isempty() == True:
            return "Stack is Empty"
        
        x = self.top
        self.top = self.top.next
        self.n = self.n - 1
        return x.data
    
    def size(self):
        
        return self.n
    
    def traverse(self):
        
        result = ""
        current = self.top
        
        while current != None:
            
            result = result + f"{current.data}" 
            current = current.next
        
        return result
    
class Stack_Array:
    
    def __init__(self,size):
        self.size = size
        self.__stack = [None] * size
        self.top = -1
        
    def push(self,value):
        if self.top == self.size - 1:
            print("Overload")
        else:
            self.top += 1
            self.__stack[self.top] = value
            
    def pop(self):
        if self.top == -1:
            print("Stack is Empty")
        else :
            data = self.__stack[self.top]
            self.top -= 1
            print(data)
            
    def traverse(self):
        
        for i in range(self.top + 1):
            print(self.__stack[i],end=" ")
        