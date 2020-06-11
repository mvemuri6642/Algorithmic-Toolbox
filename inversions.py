def _mergeSort(arr,n):
    temp=[0]*n
    return mergeSort(arr, temp, 0, n-1)





def mergeSort(arr,temp,left,right):
    inv=0
    if left<right:
        mid=(left+right)//2
        inv+=mergeSort(arr, temp, left, mid)
        inv+=mergeSort(arr, temp, mid+1, right)
        inv+=merge(arr,temp,left,mid,right)
    return inv

def merge(arr,temp,left,mid,right):
    i=k=left
    j=mid+1
    inv=0
    while(i<=mid and j<=right):
        if(arr[i]<=arr[j]):
            temp[k]=arr[i]
            k+=1
            i+=1
        else:
            temp[k]=arr[j]
            inv+=(mid-i+1)
            k+=1
            j+=1
    while(i<=mid):
        temp[k]=arr[i]
        k+=1
        i+=1
    while(j<=right):
        temp[k]=arr[j]
        k+=1
        j+=1
        
    for m in range(left,right+1):
        arr[m]=temp[m]
    return inv


m=int(input())

arr=list(map(int,input().split()))
n=len(arr)
result=_mergeSort(arr,n)
print(result)
    