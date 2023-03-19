class node:
    def __init__(self,data):
        self.data=data  
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None 
        
    
n=int(input("Enter the length of the linked list: "))
l=linked_list() #standard singly linked list
for i in range(n):
    data=int(input("Enter Data: "))
    newnode=node(data)
    if l.head==None:
        l.head=newnode 
    else:
        start=l.head
        while(start.next!=None):
            start=start.next 
        start.next=newnode 

l1=linked_list() #stack approach linked list
start=l.head 
while(start!=None):
    newnode=node(start.data)
    if l1.head==None:
        l1.head=newnode 
    else:
        newnode.next=l1.head 
        l1.head=newnode 
    start=start.next

print("The Reversed Linked List is - ")
start=l1.head 
while(start!=None):
    print(start.data,end=" ")
    start=start.next 
