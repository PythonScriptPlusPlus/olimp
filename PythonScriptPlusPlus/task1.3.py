n = 5
fact = 1
s = 0 
f = 1
for i in range(1, n+1):
	fact *= i
	s += fact * f
	f *= -1
print(s)