s=raw_input()
s1=raw_input()
f=0
for c in s:
	ix=-1
	v=s1[s.index(c)]
	if s.count(c)!=s1.count(v):
		f=1
		break
	for i in range(s.count(c)):
		ix=s.index(c,ix+1,len(s))
		if s1[ix] in v:
			continue
		f=1;
	if f==1:
		break
if f==1:
	print "not isomorphic"
else:
	print "isomorphic"
		
