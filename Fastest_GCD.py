def gcd(a,b): #euclidean algo O(n)
    
    while(b): #while b is not 0 
        
        a,b=b,a%b 
    
    return a 

t=int(input("ENTER THE NUMBER OF TEST CASES: "))

for i in range(t):
    
    a,b=map(int,input("ENTER 2 NUMBERS: ").split())
    print("GCD of",a," and ",b," = ",gcd(a,b)) #Final GCD Output

