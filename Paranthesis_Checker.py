#Use Stack Approach 

def ispar(x):
    l=[] #stack
    for i in range(len(x)):
        if x[i] in "({[":
            l+=[x[i]] #push
        else:
            if x[i]==")":
                if len(l)==0 or l[-1]!="(":
                    return False 
                else:
                    l.pop()
            elif x[i]=="}":
                if len(l)==0 or l[-1]!="{":
                    return False 
                else:
                    l.pop()
            else:
                if len(l)==0 or l[-1]!="[":
                    return False 
                else:
                    l.pop()
    return len(l)==0

t=int(input())
for i in range(t):
    x=input()
    if ispar(x)==True:
        print("Balanced")
    else:
        print("Not Balanced")
        