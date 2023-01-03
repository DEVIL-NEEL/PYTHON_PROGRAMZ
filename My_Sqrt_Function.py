#NEWTON RAPHSON METHOD OF SQUARE ROOT
def sqrt(n):
    root=n 
    try:
        while (0.5*(root+(n/root))!=root): #until the expression becomes equal to root
            root=0.5*(root+(n/root))
        return root 
    except ZeroDivisionError:
        return 0 

t=int(input("Number of Test Cases: "))  
for i in range(t):
    n=int(input("Enter ur number: "))
    ans=sqrt(n)
    print("Square Root of ",n," = ",ans)