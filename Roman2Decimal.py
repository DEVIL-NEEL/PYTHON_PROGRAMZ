def Roman2Decimal(S):
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    ans=0
    n=len(S)
    for i in range(n):
        if i!=(n-1) and d[S[i]]<d[S[i+1]]:
            ans-=d[S[i]]
        else:
            ans+=d[S[i]]
    return ans

s=input("Enter the Roman number: ")
print("The Decimal version is: ",Roman2Decimal(s))