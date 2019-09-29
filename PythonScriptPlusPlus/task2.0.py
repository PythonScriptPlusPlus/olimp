sum = 1
time = 0
n = 5

while time+1n <= n:
	sum *= n - time
	time += 1
print(sum)