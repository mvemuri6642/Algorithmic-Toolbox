def lcm(x,y):
	if(x<y):
		x,y=y,x
	while(y):
		x,y=y,x%y
	return x
a,b=list(map(int,input().split()))
res=lcm(a,b)
print(a*b//res)