class node:
    def __init__(self,data):
        self.data=data
        self.next=None 

class Queue:
    def __init__(self):
        self.head=None 
        self.tail=None 
        self.c=0
    
    def enqueue(self,data):
        newnode=node(data)
        self.c+=1
        if self.head==None:
            self.head=newnode
            self.tail=newnode 
        else:
            self.tail.next=newnode 
            self.tail=newnode 
    
    def dequeue(self):
        a=self.head.data 
        self.head=self.head.next 
        self.c-=1
        return a
    
    def n(self): #count number of elements
        return self.c 
    
    def display(self):
        start=self.head 
        while(start!=None):
            print(start.data,end=" ")
            start=start.next 
        print("\n")
    
    def peek(self):
        return self.head.data 
        
    def isempty(self):
        return self.head==None 
    

if __name__=='__main__':
    s=Queue()
    while(True):
        op=input("ENTER OPERATION NAME IN UPPERCASE. PRESS 0 TO STOP: ")
        if op=="ENQUEUE":
            n=int(input("ENTER UR DATA: "))
            s.enqueue(n)
        elif op=="DEQUEUE":
            print(s.dequeue())
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
            
        
        
    
        
    
    
    
    
    