def subArraySum(arr, n, s): 
    #Write your code here
    prev=0
    last=1 
    total=arr[0]
    while True:
        if total==s:
            return [prev+1,last]
        elif total>s and prev<(last-1):
            total-=arr[prev]
            prev+=1 
        elif last>(n-1):
            return [-1]
        else:
            total+=arr[last]
            last+=1