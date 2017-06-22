s=raw_input()
n=len(s)
l=list(s)
n=len(s);
if len(s)%2!=0:
	n=n-1
for i in range(0,n,2):
	l[i],l[i+1]=l[i+1],l[i]
s="".join(l)
print s
