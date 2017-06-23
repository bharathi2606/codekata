
d={'V':5,'X':10}
s=raw_input()
s=s.upper()
v=-1;
x=-1;
n=0
p=0
if 'V' in s:
	v=s.index('V')
	if v!=0:
		n=s.count('I',0,v)
	if v!=len(s):
		p=s.count('I',v,len(s))
	no=d['V']-n+p
	print no
else:
	if 'X' in s:
		v=s.index('X')
		if v!=0:
			n=s.count('I',0,v)
		no=d['X']-n
		print no
	else:
		print s.count('I')
