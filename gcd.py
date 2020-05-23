def gcd(x,y):
	if(x<y):
		x,y=y,x
	while(y):
		x,y=y,x%y
	return x
ab=list(map(int,input().split()))
a=int(ab[0])
b=int(ab[1])
print(gcd(a,b))
