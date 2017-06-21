x=int(input())
y=int(input())
i=2
for n in range(x,y):
	f=0
	if n<=1:
		continue
	if n==2:
		print "2"
		continue
	for i in range(2,n):
		if n%i==0:
			f=1
			break
	if f==0:
		print i+1
