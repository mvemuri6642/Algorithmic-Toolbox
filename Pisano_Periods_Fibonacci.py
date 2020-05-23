def pisano(m):
	a,b=0,1
	for i in range(0,m*m):
		c=(a+b)%m
		a,b=b,c
		if(a==0 and b==1):
			return i+1
m=int(input())
print(pisano(m))