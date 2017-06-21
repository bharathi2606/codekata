def isarmstrong(n):
	k=n
	a=str(n)
	l=len(a)
	sum=0
	while n!=0:
		r=n%10
		n=n/10
		sum=sum+(r**l)
	if sum==k:
		return 1
	else:
		return 0
x=int(input())
y=int(input())
for i in range(x,y):
	if(isarmstrong(i)):
		print i
