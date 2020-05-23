"""
GCD using naive method
best=0
gcd=input().split()
a=int(gcd[0])
b=int(gcd[1])
for d in range(1,a+b+1):
	if(a%d==0 and b%d==0):
		best=d
print(best)
"""


"""Euclid's Algorithm"""

def gcd(x,y):
	while(y):
		x,y=y,x%y
	return x
ab=list(map(int,input().split()))
a=max(ab)
b=min(ab)
print(gcd(a,b))




"""
a=3918848
b=1653264
while(b):
	if(b!=0):		
		gcd=a%b
		a=b
		b=gcd
print(a)
"""