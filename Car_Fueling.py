def car(arr,m):
    n=len(arr)
    current=0
    number=0
    while(current<n-1):
        last=current
        while(current<n-1 and arr[current+1]-arr[last]<=m):
                current+=1
        if(current==last):
            return -1
        if(current<n-1):
            number+=1
    return number
    
d=int(input())
m=int(input())
n=int(input())
arr=list(map(int,input().split()))
arr.insert(0,0)
arr.append(d)
print(car(arr,m))