#defining a Node class for linked list
class Node:
    def __init__(self,data):
        self.data=data  
        self.next=None 
    
#defining a stack class
class Stack:
    def __init__(self):
        self.head=None 
        self.c=0
    
    def push(self,data):
        newnode=Node(data)
        newnode.next=self.head 
        self.head=newnode
        self.c+=1 
        
    
    def pop(self):
        if self.head==None:
            return -1 
        else:
            a=self.head.data 
            self.head=self.head.next 
            self.c-=1
            return a  
    
    def n(self): #count function
        return self.c 
    
    def display(self):
        start=self.head 
        while(start!=None):
            print(start.data)
            start=start.next 
        
    def isempty(self):
        return self.head==None 
    
    def peek(self):
        if self.head==None:
            return -1
        else:
            return self.head.data

if __name__=='__main__':
    s=Stack()
    while(True):
        op=input("ENTER OPERATION NAME IN UPPERCASE. PRESS 0 TO STOP: ")
        if op=="PUSH":
            n=int(input("ENTER UR DATA: "))
            s.push(n)
        elif op=="POP":
            print(s.pop())
        elif op=="DISPLAY":
            s.display()
        elif op=="PEEK":
            print(s.peek())
        elif op=="COUNT":
            print(s.n())
        elif op=="ISEMPTY":
            print(s.isempty())
        elif op=="0":
            break 
        else:
            print("IMPROPER OPERATION REQUEST!!!!")
            
        
        
    
        
    
    