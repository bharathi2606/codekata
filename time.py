t1=raw_input()
t2=raw_input()
l1=t1.split(":")
l2=t2.split(":")
h1=int(l1[0])
h2=int(l2[0])
m1=int(l1[1])
m2=int(l2[1])
m=0
if h1<h2:
	h2,h1=h1,h2
	m2,m1=m1,m2
if m1>m2:
	m=m1-m2;
else:
	h1=h1-1;
	m1=m1+60
	m=m1-m2
h=h1-h2;
m=m+h*60
print m
