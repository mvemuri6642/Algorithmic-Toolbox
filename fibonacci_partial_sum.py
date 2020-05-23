m,n=list(map(int,input().split()))
arr=[]
total=0
arr.append(0)
arr.append(1)
for i in range(2,n+1):
	arr.append(arr[i-1]+arr[i-2])
for j in range(m,n+1):
	total=total+arr[j]
print(total%10)