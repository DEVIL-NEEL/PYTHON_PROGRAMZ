def max_length(l):
    curr=0
    c={0:-1}
    max_len=0
    for i in range(len(l)):
        curr+=l[i]
        if curr in c:
            max_len=max(max_len,i-c[curr])
        else:
            c[curr]=i  
    return max_len 

l=list(map(int,input("Enter Ur Array: ").split()))

print("Length of the largest subarray with sum 0 = ",max_length(l))