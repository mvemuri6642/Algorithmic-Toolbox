n=int(input())
arr=[]
arr.append(0)
arr.append(1)
for i in range(2,n+1):
	arr.append(arr[i-1]+arr[i-2])
print(arr[n])


"""
fibonacci sum squares
def fibsum(n):
	arr=[0]*(n+1)
	if(n<=1):
		return n
	arr[0]=0
	arr[1]=1
	sum=(arr[0]*arr[0])+(arr[1]*arr[1])
	for i in range(2,n+1):
		arr[i]=arr[i-1]+arr[i-2]
		sum+=arr[i]*arr[i]
	return(sum)
n=int(input())
print(fibsum(n)%10)
"""