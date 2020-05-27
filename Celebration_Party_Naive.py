def celebration(arr):
    m=len(arr)
    start=0
    current=1
    group=0
    while(current<m):
        if(arr[current]-arr[start]>1):
            start=current
            group+=1
        if(arr[current]==arr[m-1]):
            group+=1
        current+=1
    return group 
arr=list(map(float,input().split()))
print(celebration(arr))