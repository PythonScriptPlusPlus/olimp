x = int(input()) 
y = int(input()) 
test = 0
s = x * y + 1

for i in range(1,x+1):
	test += (x-(x-i))*(x-1)
test *= y 
s += test
print(s)