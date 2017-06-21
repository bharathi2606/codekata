n=int(input());
c=0;
no=n;
a=0
while n!=0:
	r=n%10
	a=a*10+r
	n=n/10
if a==no:
  print "palindrome"
else:
  print "not palindrome"
