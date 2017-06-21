n=int(input())
k=n
a=str(n)
l=len(a)
sum=0
while n!=0:
	r=n%10
	n=n/10
	sum=sum+(r**l)
print sum
if sum==k:
	print "armstrong";
else:
	print "not armstrong"
