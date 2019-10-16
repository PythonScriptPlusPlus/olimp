a = int(input()) 
b = int(input()) - 2
s = 0

repeat = round(a / 2)

if repeat < a/2:
	repeat += 2
else:
	repeat += 1

a -= 1


for i in range(0,repeat):
	s += a
	a -= 1
	s += b
	b -= 1
	
print(s)