#sum
mult = 1
n = 10
a = 0
for i in range(1,n+1):
	print(a)
	if i % 2 == 1:
		mult = 1
	else:
		mult = -1
	a = round(a + (1 + i/10) * mult, 3)
print(a)
