def sum(n):
	a,b=0,1
	for i in range(2,n+1):
		c=a+b
		c=c%10
		b,a=c,b
	return c
	
n=int(input())
x=n%60
y=(n+1)%60
if(x<=1):
	a=x
else:
	a=sum(x)
if(y<=1):
	b=y
else:
	b=sum(y)
print((a*b)%10)