s = 0
n = 10

def fact(numb):
	f = 1
	for i in range(1,numb+1):
		f *= i
	return(f)

for i in range(1,n+1):
	s += fact(i)
	
print(s)