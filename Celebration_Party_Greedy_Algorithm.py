def celebration(x):
    n=len(x)
    i=0
    group=0
    l=r=0
    while(i<=n-1):
        l=x[i]
        r=x[i]+1
        group+=1
        i+=1
        while(i<=n-1 and x[i]<=r):
            i+=1
    return group

x=list(map(float,input().split()))
print(celebration(x))