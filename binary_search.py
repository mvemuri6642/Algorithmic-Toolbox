def BinarySearch(arr2,low,high,key):
    if high<low:
        return -1
    mid=low+((high-low))//2
    if(key==arr2[mid]):
        return mid
    elif(key<arr2[mid]):
        return BinarySearch(arr2,low,mid-1,key)
    else:
        return BinarySearch(arr2, mid+1, high, key)

    
    
    
arr=[int(i) for i in input().split()]
key=[int(i) for i in input().split()]
n=arr[0]
arr2=arr[1:]
sol=[]
for i in key[1:]:
    ans=BinarySearch(arr2,0,n-1,i)
    sol.append(ans)
print(' '.join([str(i) for i in sol]))