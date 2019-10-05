m = 1
n = 10
s = 0

for i in range(1,n+1):
	s += (1+i/10)*m
	m *= -1

print(s)