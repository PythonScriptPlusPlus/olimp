n = 30
output = ''
for i in range(1,n+1):
	for j in range(1,i+1):
		output += str(j)
	print(output) 
	output = ''